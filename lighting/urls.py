from django.urls import path
from lighting import views

urlpatterns = [
    path('thiet-bi-anh-sang/', views.productList, name="lighting-list"),
    path('thiet-bi-anh-sang/<slug:slug>/',
         views.productDetail, name="lighting-detail")
]
