# -*-coding:utf-8 -*-
#
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

from django.conf.urls import patterns, url

from .views import BlogList, BlogDetail

urlpatterns = patterns(
    '',
    url(r'^/?$', BlogList.as_view(), name='blog_list'),
    url(r'^(\d)+/?$', BlogDetail.as_view(), name='blog_detail')
)