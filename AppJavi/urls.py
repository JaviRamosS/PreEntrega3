from django.urls import path
from AppJavi import views

urlpatterns = [
    path('', views.index),
    path('dogs', views.dogs),
    path('formCreateDog', views.formCreateDog),
    path('searchBreed', views.searchBreed),
    path('search/', views.search),
]