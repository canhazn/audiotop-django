from django.shortcuts import render
from django.views.generic import ListView
from project import models, serializers
from django.core.paginator import Paginator


class ProjectList(ListView):
    model = models.Project
    paginate_by = 12
    template_name = 'project_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Add in a QuerySet of all the books
        context['app_url'] = "project"
        return context


def projectList(request):
    queryset = models.Project.objects.all()
    paginator = Paginator(queryset, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    projectSerializer = serializers.ProjectSerializer(queryset, many=True)
    tagSerializer = serializers.CategorySerializer(
        models.Category.objects.all(), many=True)
    # print(serializer.data)
    context = {
        "app_url": "project",
        "projects": projectSerializer.data,
        "tags": tagSerializer.data,
        "page_obj": page_obj,
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
