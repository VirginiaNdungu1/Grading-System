# Generated by Django 2.0 on 2017-12-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0027_auto_20171215_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='due_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='upload_file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]