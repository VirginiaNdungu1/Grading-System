# Generated by Django 2.0 on 2017-12-23 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0030_remove_project_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='lec',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='sharing_modules',
        ),
        migrations.AddField(
            model_name='module',
            name='common_units',
            field=models.ManyToManyField(related_name='common_units', to='lecturer.Unit'),
        ),
        migrations.AddField(
            model_name='profile',
            name='units',
            field=models.ManyToManyField(to='lecturer.Unit'),
        ),
    ]
