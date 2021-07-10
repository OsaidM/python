from django.shortcuts import render,redirect
from .models import Dojos,ninjas
from . import views
# Create your views here.
def root(request):
    context = {
        'all_dojos': Dojos.objects.all(),
        'all_ninjas': ninjas.objects.all()
    }
    
    return render(request, 'index.html',context)

def addDojo(request):
    request.session['name'] = request.POST['name']
    request.session['city'] = request.POST['city']
    request.session['state'] = request.POST['state']
    
    newly_created_dojo = Dojos.objects.create(name = request.session['name'], city = request.session['city'], state = request.session['state'])
    return redirect('/')

def addNinja(request):
    request.session['fname'] = request.POST['first_name']
    request.session['lname'] = request.POST['last_name']
    request.session['dojo'] = request.POST['dojo']
    this_dojo = Dojos.objects.get(name = request.session['dojo'])
    newly_created_ninja = ninjas.objects.create(first_name = request.session['fname'], last_name = request.session['lname'], ninja = this_dojo)
    return redirect('/')