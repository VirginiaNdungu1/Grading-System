# Generated by Django 2.0 on 2017-12-13 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acceptance_code', models.CharField(max_length=20)),
                ('id_number', models.PositiveIntegerField()),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('gender', models.CharField(choices=[('FEMALE', 'F'), ('MALE', 'M'), ('NONE', 'None')], default=None, max_length=30)),
                ('reg_date', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
