# Generated by Django 5.0.1 on 2024-01-28 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0011_receiptitem_source_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
