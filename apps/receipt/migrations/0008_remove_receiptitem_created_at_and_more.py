# Generated by Django 5.0.1 on 2024-01-25 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0007_alter_receiptitem_receipt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receiptitem',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='receiptitem',
            name='created_by',
        ),
    ]