from django.shortcuts import render
from speaker.models import Product as SpeakerProduct


def homePage(request):
    return render(request, 'index.html')

def projectList(request):
    return render(request, 'project_list.html')