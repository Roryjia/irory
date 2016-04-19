# -*-coding:utf-8 -*-
#
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

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
    url(r'^/?$', include('blog.urls'), name='music'),
    url(r'^tool/', include('tool.urls'), name='tool'),

    # Test
    url(r'^test/', include('test.urls'), name='test')
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)