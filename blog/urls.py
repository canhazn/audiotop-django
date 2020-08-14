from django.urls import path
from blog import views

urlpatterns = [
    path('blog/', views.blogList, name="blog-list"),
    path('blog/<slug:slug>/',
         views.blogDetail, name="blog-detail")
]
