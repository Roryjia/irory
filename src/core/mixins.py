# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-07-30, by rory
# 
#

__author__ = 'rory'

import math
import six
import time
import datetime
import json

from django.db.models.query import RawQuerySet
from django.utils import timezone
from django.http import HttpResponse


class JsonResponseMixin(object):

    def render_to_json_response(self, status='0', **kwargs):
        # 错误提示
        # status='0', result={}
        # status='1', error_msg=u'无效的路由器。'
        # status='2', form_errors={}
        context = {}
        context.update(status=status, **kwargs)
        return HttpResponse(json.dumps(context), content_type='application/json')


class _Page(object):

    def __init__(self, object_list, number, num_pages, num_items):
        self.object_list = object_list
        self.number = number
        self.num_pages = num_pages
        self.num_items = num_items

    def __repr__(self):
        return '<Page %s of %s>' % (self.number, self.num_pages)

    def __len__(self):
        return len(self.object_list)

    def __getitem__(self, index):
        if not isinstance(index, (slice,) + six.integer_types):
            raise TypeError
        # The object_list is converted to a list so that if it was a QuerySet
        # it won't be a database hit per __getitem__.
        if not isinstance(self.object_list, list):
            self.object_list = list(self.object_list)
        return self.object_list[index]

    def has_next(self):
        return self.number < self.num_pages

    def has_previous(self):
        return self.number > 1

    def has_other_pages(self):
        return self.has_previous() or self.has_next()


class PaginationMixin(object):
    """
    A pagination mixin.
    Notice that this mixin relies on HttpRequest for session cache.
    """

    model = None
    items_per_page = 10

    def get_cache_key(self):
        return '{0}_{1}'.format(self.model.__name__, 'fst_req_t')

    def get_timestamp(self, key):
        t = self.request.session.get(key)
        if not t:
            return None
        t = datetime.datetime.fromtimestamp(t)
        return t

    def set_timestamp(self, key, dt):
        t = time.mktime(dt.timetuple())
        self.request.session[key] = t

    def get_datalist(self):
        """
        按查询条件得到的所有数据，返回queryset

        :return: model's queryset.
        """

        return self.model.objects.filter(is_deleted=False, is_active=True)

    def queryset(self, t):
        qs = self.get_datalist()
        return qs if isinstance(qs, RawQuerySet) else qs.filter(create_time__lte=t)

    def get_page_items(self, page):
        if not isinstance(page, int):
            page = 1
        elif page < 1:
            page = 1

        t = self.get_timestamp(self.get_cache_key())
        if not t or page == 1:
            t = timezone.localtime(timezone.now())
            self.set_timestamp(self.get_cache_key(), t)

        qs = self.queryset(t)

        # 获取总数和分页数
        total = qs.count()
        num_pages = math.ceil(total / float(self.items_per_page))

        # 获取分页数据
        if isinstance(qs, RawQuerySet):
            ctx = {
                'raw_query': qs.query.sql,
                'limit': self.items_per_page,
                'offset': (page - 1) * self.items_per_page
            }
            qs.query.sql = "{raw_query} LIMIT {limit} OFFSET {offset}".format(**ctx)
            object_list = qs
        else:
            object_list = qs[(page - 1) * self.items_per_page:page * self.items_per_page]

        return _Page(object_list=object_list, number=page, num_pages=num_pages, num_items=total)