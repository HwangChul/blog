#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/31 下午 5:33
# @Author  : 殇夜殇雪
# @File    : urls.py
from django.urls import path
from . import views
app_name = 'article'
urlpatterns = [
    path('article_list/', views.article_list, name='article_list'),

]
