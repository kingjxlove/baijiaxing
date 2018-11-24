# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: KingJX
# @Date  : 2018/11/24 12:13
""""""
from django.conf.urls import url

from baijia import views

urlpatterns = [
    url(r'^index/', views.index, name='index')
]