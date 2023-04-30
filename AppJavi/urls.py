from django.urls import path
from AppJavi import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('dogs/', views.dogs, name="dogs-list"),
    path('formCreateDog/', views.formCreateDog, name="create-dog"),
    path('searchBreed/', views.searchBreed, name="search-breed"),
    path('search/', views.search, name="result"),
    path('login', views.login_request, name="login"),
    path('register', views.register, name="register"),
]