# Generated by Django 2.0 on 2017-12-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0025_auto_20171214_0320'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
    ]