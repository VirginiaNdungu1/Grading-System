# Generated by Django 2.0 on 2017-12-23 20:38

from django.db import migrations, models
import lecturer.models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0038_auto_20171223_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(blank=True, default=lecturer.models.get_now),
        ),
    ]