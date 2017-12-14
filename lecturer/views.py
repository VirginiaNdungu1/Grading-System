from django.shortcuts import render, redirect


# Create your views here.
def lecture(request):
    return render(request, 'lecture.html')
