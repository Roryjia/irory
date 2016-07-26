# -*-coding:utf-8 -*-
# 
# Created on 2016-07-26
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

import xadmin
from django.conf import settings

from music.models import Music


class MusicAdmin(object):
    list_display = ('song_name', 'singer', 'album_name', 'show_album_image')
    model_icon = 'fa fa-music'

    def show_album_image(self, o):
        return u'<image src="{}{}" style="width:100px; height:100px" />'.format(getattr(settings, 'QINIU_QQ_MUSIC', ''), o.album_image)

    show_album_image.allow_tags = True
    show_album_image.short_description = u'封面图片'


xadmin.site.register(Music, MusicAdmin)