# -*-coding:utf-8 -*-
#
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

from django.db.models import Count, F
from django.http import Http404

from core.views import PageView, BaseView

from .models import Blog, BlogCategory


class BlogList(PageView):
    """
    博客列表
    """
    package = 'blog'
    model = Blog

    template_name = 'blog/list.html'

    def get_datalist(self):

        queryset = self.model.objects.select_related('tags').\
            filter(is_deleted=False, is_active=True)

        return queryset

    def get(self, request, *args, **kwargs):
        # 获取所有的博客分类
        cates = BlogCategory.objects.annotate(num_cates=Count('blog')).order_by('-num_cates')
        kwargs.update(cates=cates)
        return super(BlogList, self).get(request, *args, **kwargs)


class BlogDetail(BaseView):
    """
    博客详情
    """
    package = 'blog'
    template_name = 'blog/detail.html'

    def get(self, request, *args, **kwargs):
        blog = Blog.objects.select_related('tags').\
            filter(id=args[0], is_deleted=False, is_active=True).first()
        if not blog:
            raise Http404

        blog.pv = F('pv') + 1
        blog.save()

        # 获取所有的博客分类
        cates = BlogCategory.objects.annotate(num_cates=Count('blog')).order_by('-num_cates')
        kwargs.update(blog=blog, cates=cates)
        return super(BlogDetail, self).get(request, *args, **kwargs)