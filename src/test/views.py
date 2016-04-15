# -*-coding:utf-8 -*-
#
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

from core.views import BaseView


class TestView(BaseView):
    """
    测试页面
    """

    template_name = 'blog/test.html'
