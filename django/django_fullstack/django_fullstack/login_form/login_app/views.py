from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        request.session['R_f_name'] = request.POST['fname']
        request.session['R'] = 'Registered'
        newly_created_user= User.objects.create(first_name = request.POST['fname'], last_name= request.POST['lname'], email= request.POST['eml'], password= request.POST['pwd'])

        return redirect('/success')

def login(request):
    logininfo = User.objects.login(request.POST)
    if logininfo[0]: 
        request.session['eml'] = logininfo[1].email 
        messages.add_message(request, messages.SUCCESS, 'Successfully logged in!')
        return redirect('/success')
    else: 
        for error in logininfo[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')

    return redirect('/success')


def logout(request):
    request.session.clear()
    return redirect('/')

def success(request):
    return render(request, 'success.html')
