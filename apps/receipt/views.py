import pdfkit

from datetime import datetime

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from rest_framework import viewsets 
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import ReceiptSerializer, ReceiptItemSerializer, ReceiptEmptyItemSerializer
from .models import Receipt, ReceiptItem, EmptyItem

from apps.team.models import Team

class ReceiptEmptyItemViewSet(viewsets.ModelViewSet):
    serializer_class = ReceiptEmptyItemSerializer
    queryset = EmptyItem.objects.all()

class ReceiptItemViewSet(viewsets.ModelViewSet):
    serializer_class = ReceiptItemSerializer
    queryset = ReceiptItem.objects.all()

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

@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def generate_receipts(request):

    date_from_str = request.META.get('HTTP_X_DATE_FROM')
    date_to_str = request.META.get('HTTP_X_DATE_TO')
    
    # Convert string dates to datetime objects
    if date_from_str:
        date_from = datetime.strptime(date_from_str, '%Y-%m-%d')
    else:
        date_from = None

    if date_to_str:
        date_to = datetime.strptime(date_to_str, '%Y-%m-%d')
    else:
        date_to = None

    # Filter receipts by date range and user
    receipts = Receipt.objects.filter(created_by=request.user)
    if date_from:
        receipts = receipts.filter(date__gte=date_from)
    if date_to:
        # Assuming date_to is inclusive
        receipts = receipts.filter(date__lte=date_to)

    receipts = receipts.order_by('created_at')

    team = Team.objects.filter(created_by=request.user).first()

    total_amount = sum(receipt.gross_amount for receipt in receipts)

    template_name = 'receipts.html'

    template = get_template(template_name)
    html = template.render({'receipts': receipts, 'team': team, 'total_amount': total_amount, 'dateFrom': date_from_str, 'dateTo': date_to_str})
    pdf = pdfkit.from_string(html, False)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="kwity.pdf"'

    return response