# -*-coding:utf-8 -*-
# 
# Created on 2016-05-04
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

from django.db import models

from core.models import BaseModel


class Music(BaseModel):

    song_id = models.CharField(u'歌曲ID', max_length=20)
    song_name = models.CharField(u'歌曲名称', max_length=64)
    song_lyric = models.TextField(u'歌曲歌词')
    song_mp3 = models.CharField(u'歌曲MP3文件', max_length=128)
    album_name = models.CharField(u'专辑名称', max_length=64)
    album_image = models.CharField(u'专辑封面', max_length=128)
    singer = models.CharField(u'歌手名称', max_length=64)

    def __unicode__(self):
        return self.song_name

    class Meta:
        verbose_name = u'QQ巅峰榜歌曲'
        verbose_name_plural = u'QQ巅峰榜歌曲'