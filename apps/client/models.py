from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    doc_number = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=6, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='created_clients', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    modified_by = models.ForeignKey(User, related_name='modified_clients', on_delete=models.CASCADE)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return '%s' % self.name
    
    class Meta:
        ordering = ('name',)