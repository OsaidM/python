from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def root(request):
    return HttpResponse("<h1>this is the first equivalent of the @app.route('/') in flask!</h1>")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, num):
    return HttpResponse(f"placeholder to display blog number: {num}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog: {number}")

def delete(request, number):
    return redirect("/")

def json(request):
    context = {
        "name":"Noelle",
        "favourite_color":"Color of nature",
        "pets":"None :(",
        "favourite_things":["piano","WOTB","Photography"]
    }
    return render(request, "index.html", context)

# Create your views here.
