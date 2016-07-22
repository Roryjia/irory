# -*-coding:utf-8 -*-
# 
# Created on 2016-07-22
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /


import random

from core.views import BaseView
from live.models import Live


class LiveDetail(BaseView):
    """
    每日直播
    """
    package = 'live'
    template_name = 'live/detail.html'

    def get_context_data(self, **kwargs):
        live = Live.objects.all()
        if len(live):
            live = random.choice(live)
        else:
            live = None
        kwargs.update(
            live=live
        )
        return super(LiveDetail, self).get_context_data(**kwargs)