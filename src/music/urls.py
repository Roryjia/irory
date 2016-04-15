# -*-coding:utf-8 -*-
#
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

from django.conf.urls import patterns, url

from .views import MusicIndex


urlpatterns = patterns(
    '',
    url(r'^/?$', MusicIndex.as_view(), name='music_index')
)

