# Generated by Django 2.0 on 2017-12-13 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0014_auto_20171214_0133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='degree',
        ),
    ]
