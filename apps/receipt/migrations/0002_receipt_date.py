# Generated by Django 5.0.1 on 2024-01-23 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]