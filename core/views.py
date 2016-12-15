from django.http import HttpResponseRedirect
from django.shortcuts import render
from core.forms import *
from django.contrib.auth import get_user_model
from django import forms


def register(request):

    if request.method == 'POST':
        data = request.POST.copy()
        form = RegForm(request.POST)
        if form.is_valid():
            get_user_model().objects.create_user(email=form.cleaned_data['email'], password=form.cleaned_data['password1'],
                                         about_me=form.cleaned_data['about_me'],
                                         love_lang=form.cleaned_data['love_lang'],
                                         login=form.cleaned_data['login'])
            print('ok')
            return HttpResponseRedirect("/books/")
    else:
        form = RegForm()

    return render(request, "registration/register.html", {
        'form' : form
    })