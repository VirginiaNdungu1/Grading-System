from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from django.contrib import messages
from django.http import Http404
from .forms import UserProfileForm
# Create your views here.


def is_student(user):
    return user.groups.filter(name='student').exists()


def student(request):
    template_name = 'profile.html'
    return render(request, 'student.html', {'profile': template_name})


@transaction.atomic
def update_user_profile(request):
    user_id = request.user.id
    if request.method == 'POST':
        user_profile = UserProfileForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_profile.is_valid():
            user_profile.save()
            messages.success(request, 'Profile successfully updated')
            return redirect(student)
        else:
            messages.error(
                request, 'Error occured while updating,,, try again')
    else:
        user_profile = UserProfileForm(instance=request.user.profile)

    return render(request, 'account.html', {'user_profile': user_profile, })


def account(request, user_id):
    user = request.user
    user_id = user.id

    return render(request, 'profile.html',)
