# -*-coding:utf-8 -*-
#
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'修改时间', auto_now=True)

    is_active = models.BooleanField(u'是否有效', default=True)
    is_deleted = models.BooleanField(u'是否删除', default=False)

    class Meta:
        abstract = True
        ordering = ['-create_time', ]