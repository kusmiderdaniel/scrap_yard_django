# Generated by Django 5.0.1 on 2025-03-20 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0020_alter_receiptitem_sell_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptitem',
            name='sell_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
