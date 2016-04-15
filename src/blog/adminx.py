# -*-coding:utf-8 -*-
#
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

import xadmin

from .models import BlogCategory, BlogTag, Blog
from .adminforms import BlogAdminForm


class BlogCategoryAdmin(object):
    list_display = ('name', 'is_active', 'update_time')
    model_icon = 'fa fa-bookmark-o'


class BlogTagAdmin(object):
    refresh_times = (3, 5)
    model_icon = 'fa fa-bookmark'


class BlogAdmin(object):
    form = BlogAdminForm
    show_detail_fields = ['cate', 'tags']
    list_display = ('cate', 'tags', 'name', 'display_content', 'pv', 'is_top')
    model_icon = 'fa fa-book'

    def display_content(self, obj):
        return obj.content or ''

    display_content.allow_tags = True
    display_content.short_description = u'内容'

xadmin.site.register(BlogCategory, BlogCategoryAdmin)
xadmin.site.register(BlogTag, BlogTagAdmin)
xadmin.site.register(Blog, BlogAdmin)

