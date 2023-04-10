from django.urls import path
from AppJavi import views

urlpatterns = [
    path('', views.index, name="home"),
    path('dogs/', views.dogs, name="dogs-list"),
    path('formCreateDog/', views.formCreateDog, name="create-dog"),
    path('searchBreed/', views.searchBreed, name="search-breed"),
    path('search/', views.search, name="result"),
]