'''
Created on 2018-1-27
@author: Gao
'''
from django.urls import path
from . import views
urlpatterns = [
    path('', views.login),
    path('index', views.index),
    path('logout', views.logout),
]
