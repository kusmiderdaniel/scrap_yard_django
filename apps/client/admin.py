from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

admin.site.register(Client, ClientAdmin)