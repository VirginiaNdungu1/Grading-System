# Generated by Django 2.0 on 2017-12-13 16:16

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('lecturer', '0002_auto_20171213_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='pictures/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='acceptance_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('FEMALE', 'F'), ('MALE', 'M'), ('NONE', 'None')], default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128),
        ),
    ]
