from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, 'index.html')

def projectList(request):
    return render(request, 'project_list.html')