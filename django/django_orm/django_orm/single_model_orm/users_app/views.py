from django.shortcuts import render,redirect
from .models import Users
# Create your views here.
def root(request):
    context = {
        'all_users': Users.objects.all()
    }
    return render(request, 'index.html',context)

def add(request):
    request.session['fname'] = request.POST['first_name']
    request.session['lname'] = request.POST['last_name']
    request.session['email'] = request.POST['email']
    request.session['age'] = request.POST['age']
    newly_created_user = Users.objects.create(first_name=request.session['fname'], last_name = request.session['lname'], email_address = request.session['email'], age = request.session['age'])
    print(newly_created_user.id)	# view the new movie's id

    return redirect('/')