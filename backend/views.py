# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from backend.forms import LoginForm, RegisterForm

def backend_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    error_message = 'Your account is not active'
            else:
                error_message = 'Invalid Login'
    else:
        form = LoginForm()

    return render_to_response('backend/login.html', locals(),
        context_instance=RequestContext(request))

def backend_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                User.objects.create_user(form.cleaned_data['username'],
                    form.cleaned_data['password'],
                    form.cleaned_data['email']).save()
                user = authenticate(form.cleaned_data['username'], form.cleaned_data['password'])
                if user is not None:
                    user.save()
                    login(request, user)
                    return HttpResponseRedirect('/')
            except IntegrityError:
                error_message = 'User already exists'
    else:
        form = RegisterForm()

    return render_to_response('backend/register.html', locals(),
        context_instance=RequestContext(request))
