# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-07-31, by rory
# 
# 

__author__ = 'rory'


from core.views import PageView

from .models import Blog


class BlogList(PageView):
    """
    博客列表
    """
    model = Blog

    template_name = 'blog/list.html'
