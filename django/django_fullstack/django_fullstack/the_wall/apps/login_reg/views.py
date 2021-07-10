# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    return render(request, 'login_reg/index.html')

def register(request):
    reginfo = User.objects.register(request.POST)
    print(reginfo)
    if reginfo[0]: #if reginfo index 0 is TRUE
        request.session['email'] = reginfo[1].email #user email from index 1
        messages.add_message(request, messages.SUCCESS, 'Successfully registered!')
        return redirect('/success')
    else: #if reginfo index 0 is FALSE
        for error in reginfo[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')

def login(request):
    logininfo = User.objects.login(request.POST)
    if logininfo[0]: 
        request.session['email'] = logininfo[1].email 
        messages.add_message(request, messages.SUCCESS, 'Successfully logged in!')
        user = User.objects.get(email=request.session['email'])
        request.session['id'] = user.id
        return redirect('/show')
    else: 
        for error in logininfo[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')

    return redirect('/show')

def show(request):
    if 'email' in request.session:
        messages = Message.objects.all().order_by('-id')
        comments = Comments.objects.all()
        this_user = User.objects.get(id = request.session['id'])
        print(this_user, '-/'*15)
        context = {
            'messages': messages,
            'comments': comments,
            'user': this_user,
        }
        return render(request,'wall_app/wall.html',context)
    else:
        return redirect('/')

def message(request):
    Message.objects.create(user = User.objects.get(id = request.session['id']), message = request.POST['content'])
    return redirect('/show')

def comment(request):
    Comments.objects.create(message = Message.objects.get(id = request.POST['messageid']),user = User.objects.get(id = request.session['id']),comment = request.POST['content'])
    return redirect('/show')

def logout(request):
    request.session.clear()
    return redirect('/')
