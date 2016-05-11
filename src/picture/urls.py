# -*-coding:utf-8 -*-
# 
# Created on 2016-05-11
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

from django.conf.urls import patterns, url

from .views import PictureIndex


urlpatterns = patterns(
    '',
    url(r'^/?$', PictureIndex.as_view(), name='picture_index')
)