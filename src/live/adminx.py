# -*-coding:utf-8 -*-
# 
# Created on 2016-07-26
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

import xadmin

from live.models import Live


class LiveAdmin(object):
    list_display = ('live_code', 'live_name', 'is_active')
    list_editable = ('is_active', )
    model_icon = 'fa fa-film'


xadmin.site.register(Live, LiveAdmin)