from django.shortcuts import render
from django.shortcuts import render, redirect
# Create your views here.


def index(request):
    if 'visits' in request.session:
        request.session['visits'] = int(request.session['visits'])+1
    else:
        request.session['visits'] = '1'
    if 'count' in request.session:
        request.session['count'] = int(request.session['count'])+1
    else:
        request.session['count'] = '1'
    return render(request,"index.html")


def destroy(request):
    request.session.clear()
    return redirect("/")


def plus_two(request):
    request.session['count'] = int(request.session['count'])+1
    return redirect("/")


def increment_by(request):
    request.session['count'] = int(request.session['count']) + int(request.GET['increment']) - 1
    return redirect("/")