# Generated by Django 2.0 on 2017-12-23 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0037_auto_20171223_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]