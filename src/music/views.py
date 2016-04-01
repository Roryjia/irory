# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-07-30, by rory
# 
# 

__author__ = 'rory'


from core.views import BaseView


class MusicIndex(BaseView):
    """
    每日推荐音乐
    """
    package = 'music'
    template_name = 'music/index.html'

