# Generated by Django 5.0.1 on 2024-01-25 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_alter_item_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='receipt',
        ),
    ]
