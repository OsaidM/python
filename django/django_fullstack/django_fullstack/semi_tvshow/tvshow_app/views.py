from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Show
# Create your views here.
def root(request):

    context = {
        'all_shows': Show.objects.all(),
    }

    return render(request, 'index.html',context)


def new(request):
    context = {
        'all_shows': Show.objects.all(),
    }
    
    return render(request, 'new_show.html',context)

def add_new(request):
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/new')
    else:
        new_show_create = Show.objects.create(network = request.POST['network'],title= request.POST['title'], desc = request.POST['desc'], release_date = request.POST['release_date'])
        messages.success(request, "Show successfully Added")
        return redirect('/')



def edit(request, id):
    context = {
        'all_shows': Show.objects.all(),
        'this_show': Show.objects.get(id = id)
    }

    return render(request, 'edit_show.html', context)

def edit_show(request,id):
    
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/shows/'+ format(id) +'/edit')
    else:
        show_to_update = Show.objects.get(id=id)
        show_to_update.network = request.POST['network']
        show_to_update.title = request.POST['title']
        show_to_update.description = request.POST['desc']
        show_to_update.release_date = request.POST['release_date']
        show_to_update.save()	# then -0
        messages.success(request, "Show Successfully Updated")
        return redirect('/')

def show(request, id):
    context = {
        'all_shows': Show.objects.all(),
        'this_show': Show.objects.get(id = id)
    }
    request.session['id'] = id
    

    return render(request, 'show_info.html',context)


def delete(request, id):
    Show.objects.get(id=id).delete()
    return redirect("/")