# -*-coding:utf-8 -*-
# 
# Created on 2016-05-11
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /


from core.views import BaseView
from music.models import Music


class PictureIndex(BaseView):
    """
    每日推荐音乐
    """
    package = 'picture'
    template_name = 'picture/list.html'

    def get_context_data(self, **kwargs):
        kwargs.update(
            music=Music.objects.all()
        )
        return super(PictureIndex, self).get_context_data(**kwargs)