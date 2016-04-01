# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-07-31, by rory
# 
# 

__author__ = 'rory'

from django.http import Http404

from core.views import PageView, BaseView

from .models import Blog


class BlogList(PageView):
    """
    博客列表
    """
    package = 'blog'
    model = Blog

    template_name = 'blog/list.html'

    def get_datalist(self):

        queryset = self.model.objects.select_related('tags').\
            filter(is_deleted=False, is_active=True)
        return queryset


class BlogDetail(BaseView):
    """
    博客详情
    """
    package = 'blog'
    template_name = 'blog/detail.html'

    def get(self, request, *args, **kwargs):
        blog = Blog.objects.select_related('tags').\
            filter(id=args[0], is_deleted=False, is_active=True).first()
        if not blog:
            raise Http404

        kwargs.update(blog=blog)
        return super(BlogDetail, self).get(request, *args, **kwargs)