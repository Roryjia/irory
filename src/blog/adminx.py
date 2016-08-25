# -*-coding:utf-8 -*-
#
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

import xadmin

from .models import BlogCategory, BlogTag, Blog, BlogView
from .adminforms import BlogAdminForm


class BlogCategoryAdmin(object):
    list_display = ('name', 'is_active', 'update_time')
    model_icon = 'fa fa-bookmark-o'


class BlogTagAdmin(object):
    refresh_times = (3, 5)
    list_display = ('name', 'is_active', 'update_time')
    model_icon = 'fa fa-bookmark'


class BlogAdmin(object):
    form = BlogAdminForm
    # show_detail_fields = ['cate', 'tags']
    list_display = ('name', 'pv', 'cate', 'tags', 'is_top')
    model_icon = 'fa fa-book'
    ordering = ['-pv', ]

    # def display_content(self, obj):
    #     return obj.content or ''

    # display_content.allow_tags = True
    # display_content.short_description = u'内容'


class BlogViewAdmin(object):
    list_display = ('blog', 'ip', 'city', 'create_time')
    model_icon = 'fa fa-eye'
    ordering = ['-create_time', ]


xadmin.site.register(BlogCategory, BlogCategoryAdmin)
xadmin.site.register(BlogTag, BlogTagAdmin)
xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(BlogView, BlogViewAdmin)

