# Generated by Django 5.0.1 on 2024-01-22 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_rename_unit_price_item_buy_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='modified_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='item',
            name='modified_at',
        ),
        migrations.RemoveField(
            model_name='item',
            name='modified_by',
        ),
    ]