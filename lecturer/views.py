from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from django.contrib import messages
from django.http import Http404
from .forms import UserProfileForm, CreateProjectForm
from .models import Unit, Project
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
            return redirect(lecture)
    else:
        form = CreateProjectForm()
    return render(request, 'create_project.html', {"form": form})


def units(request, unit_code):
    unit = Unit.objects.get(id=unit_code)
    unit_id = unit.id
    return render(request, 'units.html', {'unit': unit})


def get_unit_projects(request, unit_code):
    unit = Unit.objects.get(id=unit_code)
    unit_id = unit.id
    ind_ass = []
    group_ass = []
    cats = []
    mid_exams = []
    projects = Project.objects.filter(unit_id=unit_id).all()
    for project in projects:
        if project.assessment_type_id == 1:
            ind_ass.append(project)
        elif project.assessment_type_id == 2:
            group_ass.append(project)
        elif project.assessment_type_id == 3:
            cats.append(project)
        elif project.assessment_type_id == 4:
            mid_exams.append(project)
    return render(request, 'projects.html', {"unit": unit, "projects": projects, "ind_ass": ind_ass, "group_ass": group_ass, "cats": cats, "mid_exams": mid_exams})
