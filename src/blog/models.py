# -*-coding:utf-8 -*-
#
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

from django.db import models

from core.models import BaseModel


class BlogCategory(BaseModel):
    name = models.CharField(u'分类名称', max_length=32)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'博客分类'
        verbose_name_plural = u'博客分类'


class BlogTag(BaseModel):
    name = models.CharField(u'标签名称', max_length=32)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'博客标签'
        verbose_name_plural = u'博客标签'


class Blog(BaseModel):
    cate = models.ForeignKey(BlogCategory, verbose_name=u'博客分类')
    tags = models.ManyToManyField(BlogTag, verbose_name=u'博客标签')

    name = models.CharField(u'名称', max_length=64)
    content = models.TextField(u'内容', max_length=64)

    pv = models.IntegerField(u'浏览量', default=0)
    is_top = models.BooleanField(u'是否置顶', default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'博客'
        verbose_name_plural = u'博客'


class BlogView(BaseModel):
    blog = models.ForeignKey(Blog, verbose_name=u'博客')
    ip = models.IPAddressField(verbose_name=u'IP')
    city = models.CharField(max_length=100, verbose_name=u'城市')

    def __unicode__(self):
        return u'{} - {}'.format(self.blog, self.ip)

    class Meta:
        verbose_name = u'博客浏览'
        verbose_name_plural = u'博客浏览'


class BlogLink(BaseModel):
    name = models.CharField(max_length=100, verbose_name=u'名称')
    site = models.URLField(verbose_name=u'站点URL')
    order = models.IntegerField(verbose_name=u'排序')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'博客链接'
        verbose_name_plural = u'博客链接'