# Generated by Django 2.0 on 2017-12-14 00:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lecturer', '0023_auto_20171214_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('link', models.CharField(blank=True, max_length=140)),
                ('upload_file', models.FileField(upload_to='')),
                ('additional_notes', models.TextField(max_length=500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='lecturer.Assessment')),
                ('lec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_lec', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]