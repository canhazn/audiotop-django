from django.urls import path
from browser import views

urlpatterns = [
    path('', views.homePage, name="trang-chu"),
    path('du-an-noi-bat/', views.projectList, name="du-an-noi-bat"),
    # path('thiet-bi-am-thanh/', views.projectList, name="thiet-bi-am-thanh"),
    path('thiet-bi-anh-sang/', views.projectList, name="thiet-bi-anh-sang")
]
