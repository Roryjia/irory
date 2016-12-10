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

from .models import Blog, BlogCategory, BlogView, BlogLink


class BlogList(PageView):
    """
    博客列表
    """
    package = 'blog'
    model = Blog

    template_name = 'blog/list.html'

    cate = None

    items_per_page = 5
    object_list_template_name = 'blog/blog_piece.html'

    def get_datalist(self):
        queryset = self.model.objects
        if self.cate:
            queryset = queryset.filter(cate=self.cate)
        queryset = queryset.select_related('tags').filter(is_deleted=False, is_active=True).order_by('-is_top', '-pv')
        return queryset

    def get(self, request, *args, **kwargs):

        # 按着分类搜索
        cid = request.GET.get('cid', '')
        if cid:
            if not cid.isdigit():
                raise Http404
            try:
                self.cate = BlogCategory.objects.get(id=cid)
            except BlogCategory.DoesNotExist:
                raise Http404

        # 获取所有的博客分类
        cates = BlogCategory.objects.annotate(num_cates=Count('blog')).order_by('-num_cates')
        links = BlogLink.objects.order_by('order')
        kwargs.update(cates=cates, links=links, cid=cid)
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

        # 记录博客浏览量
        blog.pv = F('pv') + 1
        blog.save()

        # 详细记录客户端情况
        BlogView(blog=blog, ip=self._ip, city=self._city, refer=self.request.META.get('HTTP_REFERER', '')).save()

        # 获取所有的博客分类
        cates = BlogCategory.objects.annotate(num_cates=Count('blog')).order_by('-num_cates')
        links = BlogLink.objects.order_by('order')
        kwargs.update(blog=blog, cates=cates, links=links)
        return super(BlogDetail, self).get(request, *args, **kwargs)