# Generated by Django 4.0.4 on 2022-07-13 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fupresystem', '0005_remove_login_staffname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='applications',
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]