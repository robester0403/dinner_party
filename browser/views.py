from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe


def index(request):
    return render(request, 'browser/index.html')

# let's just start with something simple and bring up items without sorting or filtering

# get all items

def foodtype(request, main_type):
    recipes = Recipe.objects.filter(main_type=main_type)
    context = {'recipes': recipes}
    return render(request, 'browser/allitems.html', context)

def allitems(request):
    # recipes = Recipe.objects.all().distinct('main_type')
    recipes = Recipe.objects.all()
    context = {'recipes' : recipes}
    return render(request, 'browser/allitems.html', context)


# trying to get a certain type
def country(request):
    # recipes = Recipe.objects.filter(country=country)
    country = Recipe.COUNTRY
    context = {'country': country}
    return render(request, 'browser/country.html', context)

# def countryquery(request, country_selection):


# get an item 
def pksearch(request, id):
    recipes = Recipe.objects.get(id=id)
    context = {'recipes' : recipes}
    return render(request, 'browser/allitems.html', context)


# 'recipes' is the one in the template

# Server doesn't run because all the views have not been made yet