# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-06-30, by rory
# 
# 

__author__ = 'rory'

from django.conf.urls import patterns, url, include

import xadmin
xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = patterns(
    '',

    url(r'^xadmin/', include(xadmin.site.urls), name='xadmin'),
    url(r'^ckeditor/', include('ckeditor.urls'), name='ckeditor'),
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)