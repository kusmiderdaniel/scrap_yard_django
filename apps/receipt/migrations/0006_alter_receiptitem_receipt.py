# Generated by Django 5.0.1 on 2024-01-25 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0005_receiptitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptitem',
            name='receipt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='receipt.receipt'),
        ),
    ]
