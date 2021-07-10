from django.shortcuts import render, HttpResponse

# Create your views here.
def root(request):
    return render(request,"index.html")

def handle(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['dojo_location']
    request.session['language'] = request.POST['f_language']
    request.session['comment'] = request.POST['comment']

    request.session['gender'] = request.POST['gender']
    request.session['genres'] = request.POST.getlist('genres')
    
    
    return render(request,"info.html")