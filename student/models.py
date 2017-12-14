from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
import lecturer
# Create your models here.


class Submission(models.Model):
    student_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='student')
    project = models.ForeignKey(
        'lecturer.Project', on_delete=models.CASCADE, related_name='project')
    title = models.CharField(max_length=140)
    link = models.CharField(max_length=140, blank=True)
    upload_file = models.FileField()
    additional_notes = models.TextField(max_length=500)

    def __str__(self):
        return self.title
