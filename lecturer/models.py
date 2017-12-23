from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
import student
import weekday_field
from datetime import datetime as dt

# Create your models here.

alphanumeric = RegexValidator(
    r'^[0-9a-zA-Z]*/$', 'Only alphanumeric characters are allowed.')

ROLE_CHOICES = (
    ('STUDENT', 'Student'),
    ('LECTURER', 'Lecturer'),
    ('DEAN', 'Dean'),
)

GENDER_CHOICES = (
    ('FEMALE', 'F'),
    ('MALE', 'M'),
    ('NONE', 'None')
)

DAYS_OF_WEEK = (
    ('SUNDAY', 'Sun'),
    ('MONDAY', 'Mon'),
    ('TUESDAY', 'Tue'),
    ('WEDNESDAY', 'Wed'),
    ('THURSDAY', 'Thurs'),
    ('FRIDAY', 'Fri'),
    ('SATURDAY', 'Sat')
)


def get_now():
    return dt.now().strftime("%d/%m/%Y")


class Days(models.Model):
    days = models.CharField(max_length=30, choices=DAYS_OF_WEEK)

    def __str__(self):
        return self.days


class Program(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.code


class Unit(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    venue = models.CharField(max_length=50, null=True)
    unit_days = models.ManyToManyField(Days)
    start_time = models.TimeField(auto_now_add=False, null=True)
    stop_time = models.TimeField(auto_now_add=False, null=True)
    exam_date = models.DateTimeField(auto_now_add=False, null=True)

    def __str__(self):
        return self.code


class Module(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    enrolled_students = models.ManyToManyField(
        User, related_name='enrolled_students')
    common_units = models.ManyToManyField(
        Unit, related_name='common_units')

    def __str__(self):
        return self.code


class Assessment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='lecturer')
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Project(models.Model):
    lec = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='unit_lec')
    title = models.CharField(max_length=140)
    link = models.CharField(max_length=140, blank=True)
    upload_file = models.FileField(blank=True)
    additional_notes = models.TextField(max_length=500, blank=True)
    assessment_type = models.ForeignKey(
        Assessment, related_name="assessment", on_delete="models.CASCADE", null=True)
    submissions = models.ManyToManyField(
        'student.Submission', related_name='submitted_projects', blank=True)
    due_date = models.DateTimeField(default=get_now, blank=True)
    due_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    acceptance_code = models.CharField(max_length=20, blank=True)
    profile_pic = models.ImageField(upload_to='pictures/', blank=True)
    id_number = models.PositiveIntegerField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)
    roles = models.CharField(max_length=30, choices=ROLE_CHOICES, blank=True)
    gender = models.CharField(
        max_length=30, choices=GENDER_CHOICES, default='NONE', blank=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    programs = models.ManyToManyField(
        Program)
    modules = models.ManyToManyField(Module)
    units = models.ManyToManyField(
        Unit)

    def __str__(self):
        return self.user.username + '' + self.user.first_name


User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
