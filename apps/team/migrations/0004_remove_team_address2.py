# Generated by Django 5.0.1 on 2024-02-02 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_team_short_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='address2',
        ),
    ]