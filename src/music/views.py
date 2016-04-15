# -*-coding:utf-8 -*-
#
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

from core.views import BaseView


class MusicIndex(BaseView):
    """
    每日推荐音乐
    """
    package = 'music'
    template_name = 'music/index.html'

