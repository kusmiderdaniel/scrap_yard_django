import pdfkit

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template

from rest_framework import viewsets 
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import ReceiptSerializer, ReceiptEmptyItemSerializer
from .models import Receipt, EmptyItem

from apps.team.models import Team

class ReceiptEmptyItemViewSet(viewsets.ModelViewSet):
    serializer_class = ReceiptEmptyItemSerializer
    queryset = EmptyItem.objects.all()

class ReceiptViewSet(viewsets.ModelViewSet):
    serializer_class = ReceiptSerializer
    queryset = Receipt.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        team = self.request.user.teams.first()
        team.save()

        serializer.save(created_by=self.request.user, team=team, modified_by=self.request.user)
    
    def perform_update(self, serializer):
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied('Wrong object owner')
    
        serializer.save()

@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def generate_pdf(request, receipt_id):
    receipt = get_object_or_404(Receipt, pk=receipt_id, created_by=request.user)
    team = Team.objects.filter(created_by=request.user).first()

    template_name = 'pdf.html'

    template = get_template(template_name)
    html = template.render({'receipt': receipt, 'team': team})
    pdf = pdfkit.from_string(html, False, options={'orientation': 'Landscape'})

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="receipt.pdf"'

    return response
