# -*-coding:utf-8 -*-
# 
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /


from django.conf.urls import patterns, url

from .views import ValidateCodeView, QrcodeView

urlpatterns = patterns(
    '',
    url('^code/?$', ValidateCodeView.as_view(), name='validate_view'),
    url('^qrcode/?$', QrcodeView.as_view(), name='qrcode_view'),
)