# -*-coding:utf-8 -*-
# 
# Created on 2016-07-22
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /


from core.views import BaseView
from live.models import Live


class LiveDetail(BaseView):
    """
    每日直播
    """
    package = 'live'
    template_name = 'live/detail.html'

    def get(self, request, *args, **kwargs):
        live = Live.objects.filter(live_code=args[0]).first()
        kwargs.update(
            live=live
        )

        return super(LiveDetail, self).get(request, *args, **kwargs)