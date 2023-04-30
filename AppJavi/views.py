from django.shortcuts import render
from AppJavi.models import Dog
from AppJavi.forms import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index(request):

    return render(request, "AppJavi/index.html")

def about(request):

    return render(request, "AppJavi/about.html")

def dogs(request):

    dogs = Dog.objects.all()
    
    return render(request, "AppJavi/dogs.html", {'dogs':dogs})

def formCreateDog(request):

    if request.method == 'POST':

        dog = Dog(name=request.POST['name'], breed=request.POST['breed'], age=request.POST['age'], owner_name=request.POST['owner_name'])
        dog.save()

    my_form = FormCreateDog()

    return render(request, "AppJavi/formCreateDog.html", {"my_form": my_form})

def searchBreed(request):

    dogs = Dog.objects.all()
    search_form = SearchBreed()

    return render(request, "AppJavi/searchBreed.html", {'dogs': dogs, 'search_form': search_form})

def search(request):
    
    if request.GET["breed"]:

        breed = request.GET['breed']
        dogs = Dog.objects.filter(breed__icontains=breed)

        return render(request, "AppJavi/searchResult.html", {"dogs":dogs, "breed":breed})

    else:
        response = "Couldn't make search"

    return HttpResponse(response)

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get['username']
            password = form.cleaned_data.get['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return render(request, "AppJavi/index.html", {"mensaje": f"Welcome {username}"})
            else:
                return render(request, "AppJavi/index.html", {"mensaje": "Error. Wrong information."})
        
        else:

            return render (request, "AppJavi/index.html", {"mensaje": "Error. Wrong form."})
    
    form = AuthenticationForm()
    
    return render(request, "AppJavi/index.html", {"form":form})

def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppJavi/index.html", {"mensaje":"User created"})

        else:
            form = UserCreationForm()
        
        return render(request, "AppJavi/register.html", {"form":form})
