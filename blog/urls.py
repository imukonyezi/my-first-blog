# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 18:41:58 2016

@author: imuko
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]