# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from . import forms
from .models import Image,Profile

# Create your views here.

def homePage(request):
    postImage=Image.objects.all().order_by('imageTime')
    return render(request,'social/homePage.html',{'images':postImage})
@login_required(login_url='/accounts/')
def postImage(request):
    currentUser=request.user
    if request.method=='POST':
        form=forms.PostImage(request.POST,request.FILES)
        if form.is_valid():
            imageInstance=form.save(commit=False)
            imageInstance.userF=currentUser
            imageInstance.save()
            return redirect('instaSocial:homePage')
    else:
        form=forms.PostImage()

    return render (request,'social/postImage.html',{'form':form})

def searchUser(request):
    if 'user' in request.GET and request.GET['user']:
        search_term=request.GET.get('user')
        images=Image.searchImageByUser(search_term)
        # message = f"{search_term}"

        return render(request,'social/search.html',{'images':images})
    else:
        message='no search yet'
        return render(request,'social/search.html',{'message':message})





##########################################################################################

def signUp(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('instaSocial:logIn')
    else:
        form=UserCreationForm()
    return render(request,'auth/signUp.html',{'form':form})

def logIn(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('instaSocial:homePage')
    else:
        form=AuthenticationForm()
    return render(request,'auth/logIn.html',{'form':form})

def logOut(request):
    if request.method=='POST':
        logout(request)
        return redirect('instaSocial:logIn')
@login_required(login_url='/accounts/')
def createProfile(request):
    current_user = request.user
    if request.method=='POST':
        form=forms.CreateProfile(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.userF=current_user
            profile.save()

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('instaSocial:viewProfile' )
    else:
        form=forms.CreateProfile()
    return render(request,'auth/createProfile.html',{'form':form})

def viewProfile(request,pk=None):
    # profile=Profile.objects.all()
    # return render(request,'auth/profile.html',{'profiles':profile})
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    # args = {'user': user}
    return render(request, 'auth/profile.html', {'user': user})
