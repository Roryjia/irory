# -*-coding:utf-8 -*-
# 
# Created on 2016-07-22
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /


from django.conf.urls import patterns, url

from .views import LiveDetail


urlpatterns = patterns(
    '',
    url(r'^detail/?$', LiveDetail.as_view(), name='live_detail')
)