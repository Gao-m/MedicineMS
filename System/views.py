"""
Created on 2018-1-27
@author: Gao
"""
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as sys_login, logout as sys_logout
from django.contrib.auth.decorators import login_required


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/index')
    else:
        if request.method == 'GET':
            return render(request,'login.html')
            #return render_to_response('login.html')
        else:
            if 'username' in request.POST and 'password' in request.POST:
                user = authenticate(username=request.POST['username'], password=request.POST['password'])
                if user is not None:
                    sys_login(request, user)
            return HttpResponseRedirect('/index')


def logout(request):
    sys_logout(request)
    return HttpResponseRedirect('/index')


@login_required
def index(request):
    return render_to_response("index.html", {"user": request.user})
