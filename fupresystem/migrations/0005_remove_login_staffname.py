# Generated by Django 4.0.4 on 2022-07-13 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fupresystem', '0004_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='staffname',
        ),
    ]
