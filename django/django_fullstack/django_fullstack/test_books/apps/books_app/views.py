from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def root(request):

    return render(request,'books_app/index.html')

def register(request):
    create_user = User.objects.register_validator(request.POST)
    print(create_user)
    return redirect('/')