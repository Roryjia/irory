# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-07-31, by rory
# 
# 

__author__ = 'rory'


from django.conf.urls import patterns, url

from .views import BlogList, BlogDetail

urlpatterns = patterns(
    '',
    url(r'^/?$', BlogList.as_view(), name='blog_list'),
    url(r'^(\d)+/?$', BlogDetail.as_view(), name='blog_detail')
)