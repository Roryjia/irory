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

    # 公用第三方
    url(r'^xadmin/', include(xadmin.site.urls), name='xadmin'),
    url(r'^ckeditor/', include('ckeditor.urls'), name='ckeditor'),

    # 各个模块
    url(r'^blog/', include('blog.urls'), name='blog'),
    url(r'^music/', include('music.urls'), name='music'),
    url(r'^/?$', include('music.urls'), name='music'),

    # Test
    url(r'^test/', include('test.urls'), name='test')
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)