# -*-coding:utf-8 -*-
# 
# Created on 2016-07-22
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

from django.db import models

from core.models import BaseModel


class Live(BaseModel):

    live_code = models.CharField(u'直播标识', max_length=100)
    live_name = models.CharField(u'直播名称', max_length=100)
    live_m3u8 = models.TextField(u'直播M3U8')

    def __unicode__(self):
        return self.live_name

    class Meta:
        verbose_name = u'直播'
        verbose_name_plural = u'直播'