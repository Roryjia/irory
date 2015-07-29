# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-07-01, by rory
# 
# 

__author__ = 'rory'

from django.conf import settings
from django.utils import timezone


def global_variate(request):
    return {
        'site_name': getattr(settings, 'SITE_NAME', 'http://rory.jia'),
        'current_year': timezone.now().year
    }

