# -*-coding:utf-8 -*-
#
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

import IP
from django.views.generic import TemplateView

from .mixins import JsonResponseMixin, PaginationMixin


class BaseView(TemplateView):

    package = None

    def get_context_data(self, **kwargs):
        kwargs = super(BaseView, self).get_context_data(**kwargs)
        kwargs.update(package=self.package)
        return kwargs

    @property
    def _ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR', '')
        return ip

    @property
    def _city(self):
        try:
            return IP.find(self._ip).split('\t')[-1]
        except Exception as e:
            return ''


class PageView(PaginationMixin, JsonResponseMixin, BaseView):
    """
    A view for pagination.
    """

    object_list_template_name = None

    key_name = 'page'

    page_range_left = 3
    page_range_right = 3

    def get_template_names(self):
        if self.request.is_ajax() and self.object_list_template_name:
            return [self.object_list_template_name]

        return super(PageView, self).get_template_names()

    def get_page_data(self, object_list):
        return object_list

    def get_param_list(self):
        params_list = super(PageView, self).get_param_list()
        params_list.append(self.key_name)
        return params_list

    def get_datalist(self):
        """
        Rewrite this func to satisfy your own query needs.
        """

        return super(PageView, self).get_datalist()

    def get(self, request, *args, **kwargs):
        try:
            page = int(request.GET.get(self.key_name))
        except (ValueError, TypeError):
            page = 1

        paginator = self.get_page_items(page)

        context = {
            'num_pages': paginator.num_pages,
            'num_items': paginator.num_items,
            'current_page': paginator.number,
            'has_next': paginator.has_next(),
            'items': self.get_page_data(paginator.object_list)
        }
        context.update(self.get_context_data(**kwargs))

        res = self.render_to_response(context=context, content_type=None)
        if request.is_ajax():
            data = {
                'html': res.rendered_content,
                'has_next': context['has_next']
            }
            return self.render_json_to_response(result=data)
        return res