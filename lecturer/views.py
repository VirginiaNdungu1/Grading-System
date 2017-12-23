from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from django.contrib import messages
from django.http import Http404
from .forms import UserProfileForm, CreateProjectForm
from .models import Unit
# Create your views here.


def is_lecturer(user):
    return user.groups.filter(name='lecturer').exists()


def lecture(request):
    user = request.user
    profile_id = user.id
    units = user.profile.units.all()
    return render(request, 'lecture.html', {'units': units, })


@transaction.atomic
def update_user_profile(request):
    user_id = request.user.id
    if request.method == 'POST':
        user_profile = UserProfileForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_profile.is_valid():
            user_profile.save()
            messages.success(request, 'Profile successfully updated')
            return redirect(lecture)
        else:
            messages.error(
                request, 'Error occured while updating,,, try again')

    else:
        user_profile = UserProfileForm(instance=request.user.profile)

    return render(request, 'account.html', {'user_profile': user_profile, })


@login_required(login_url='/accounts/login/')
def discover(request):
    return render(request, 'discover.html')


def account(request, user_id):
    user = request.user
    user_id = user.id
    lec_id = user_id
    return render(request, 'profile.html',)


def create_project(request):
    user = request.user
    lec_id = user.id
    if request.method == 'POST':
        form = CreateProjectForm(request.POST, request.FILES)
        if user.is_authenticated and form.is_valid():
            project = form.save(commit=False)
            project.lec_id = lec_id
            project.save()
    else:
        form = CreateProjectForm()
    return render(request, 'create_project.html', {"form": form})
