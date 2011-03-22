# Create your views here.
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from backend.forms import LoginForm

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

