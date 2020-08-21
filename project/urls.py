from django.urls import path
from project import views


urlpatterns = [
    path('du-an-noi-bat/', views.ProjectList.as_view(), name="project-list"),
    path('du-an-noi-bat/<slug:slug>/', views.projectDetail, name="project-detail")
]
