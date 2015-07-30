# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-07-30, by rory
# 
# 

__author__ = 'rory'

from django.conf.urls import patterns, url

from .views import TestView

urlpatterns = patterns(
    '',
    url('^/?$', TestView.as_view(), name='test_view')
)