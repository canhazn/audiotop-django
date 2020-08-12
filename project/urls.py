from django.urls import path
from project import views


urlpatterns = [
    path('du-an-noi-bat/', views.projectList, name="project-list"),
    path('du-an-noi-bat/<slug:slug>/', views.projectDetail, name="project-detail")
]
