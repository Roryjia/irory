# -*-coding:utf-8 -*-
#
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

import random

from django.conf import settings

from core.views import BaseView
from music.models import Music


class MusicIndex(BaseView):
    """
    每日推荐音乐
    """
    package = 'music'
    template_name = 'music/list.html'

    def get_context_data(self, **kwargs):
        _s = random.choice(xrange(1, 102))
        kwargs.update(
            music=Music.objects.order_by('-id').all()[_s:_s + 20],
            QINIU_URL=getattr(settings, 'QINIU_QQ_MUSIC', '')
        )
        return super(MusicIndex, self).get_context_data(**kwargs)
