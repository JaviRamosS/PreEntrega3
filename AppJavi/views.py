from django.shortcuts import render
from AppJavi.models import Dog
from AppJavi.forms import *
from django.http import HttpResponse

# Create your views here.
def index(request):

    return render(request, "AppJavi/index.html")

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