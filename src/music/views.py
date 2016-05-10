# -*-coding:utf-8 -*-
#
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

from core.views import BaseView
from music.models import Music


class MusicIndex(BaseView):
    """
    每日推荐音乐
    """
    package = 'music'
    template_name = 'music/list.html'
    # template_name = 'music/index.html'
    # template_name = 'test/music-1.html'

    def get_context_data(self, **kwargs):
        kwargs.update(
            music=Music.objects.all()[20:40]
        )
        return super(MusicIndex, self).get_context_data(**kwargs)

    # def get(self, request, *args, **kwargs):
    #     kwargs.update(
    #         music=Music.objects.all()
    #     )
    #     return super(MusicIndex, self).get()

