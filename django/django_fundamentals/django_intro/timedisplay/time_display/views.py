from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def root(request):
    context = {
        'time': strftime("%Y-%m-%d-%A -------- %H:%M:%S %p",gmtime())
    }
    return render(request,"index.html", context)
