from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def create_user(request):
    print("Got Post Info ...............")
    print(request.POST)
    
    get_name= request.POST['name']
    get_email= request.POST['email']

    data = {
        'name' : get_name,
        'email' : get_email,
    }

    print(get_name)
    print(get_email)

    return redirect('/success')

def success(request):
    return render(request,'success.html')
