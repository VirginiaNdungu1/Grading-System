# Generated by Django 2.0 on 2017-12-13 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lecturer', '0006_auto_20171213_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course', to=settings.AUTH_USER_MODEL),
        ),
    ]
