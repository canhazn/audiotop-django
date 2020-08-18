from django.shortcuts import render
from project import models, serializers


def projectList(request):
    queryset = models.Project.objects.all()
    projectSerializer = serializers.ProjectSerializer(queryset, many=True)
    tagSerializer = serializers.CategorySerializer(
        models.Category.objects.all(), many=True)
    # print(serializer.data)
    context = {
        "app_url": "project",
        "projects": projectSerializer.data,
        "tags": tagSerializer.data,
        "message": "hello"
    }
    return render(request, 'project_list.html', context)


def projectDetail(request, slug):
    queryset = models.Project.objects.get(slug=slug)
    # projectSerializer = serializers.ProjectSerializer(models.Project, slug=slug)
    tags = queryset.tags.all()
    context = {
        "app_url": "project",
        "project": queryset,

    }

    return render(request, "project_detail.html", context)
