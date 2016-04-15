# -*-coding:utf-8 -*-
#
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

from django.conf import settings
from django.utils import timezone


def global_variate(request):
    return {
        'site_name': getattr(settings, 'SITE_NAME', 'http://rory.jia'),
        'current_year': timezone.now().year
    }

