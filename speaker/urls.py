from django.urls import path
from speaker import views

urlpatterns = [
    path('thiet-bi-am-thanh/', views.productList, name="speaker-list"),
    path('thiet-bi-am-thanh/<slug:slug>/', views.productDetail, name="speaker-detail")
]
