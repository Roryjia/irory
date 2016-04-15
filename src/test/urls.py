# -*-coding:utf-8 -*-
#
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

from django.conf.urls import patterns, url

from .views import TestView

urlpatterns = patterns(
    '',
    url('^/?$', TestView.as_view(), name='test_view'),
)