from django.shortcuts import render
from speaker.models import Product as SpeakerProduct
from project import serializers, models


def homePage(request):
    queryset = models.Project.objects.all()[0:9]
    serializer = serializers.ProjectSerializer(queryset, many=True)

    return render(request, 'index.html', { "app_url": "home", "projects": serializer.data})

