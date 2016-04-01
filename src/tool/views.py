# -*-coding:utf-8 -*-
# 
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

import StringIO

import qrcode
from django.http import HttpResponse

from core.views import BaseView
from .validate_code import create_validate_code


class ValidateCodeView(BaseView):
    """
    生成验证码图片
    """

    def get(self, request, *args, **kwargs):
        io = StringIO.StringIO()
        img, code = create_validate_code()
        img.save(io, 'GIF')
        return HttpResponse(io.getvalue(), content_type='image/gif')


class QrcodeView(BaseView):
    """
    生成二维码
    """

    def get(self, request, *args, **kwargs):
        content = self.request.GET.get('content', 'http://www.google.com')

        qr = qrcode.QRCode(version=5, box_size=10, error_correction=qrcode.ERROR_CORRECT_L)
        qr.add_data(content)
        qr.make(fit=True)
        img = qr.make_image()
        io = StringIO.StringIO()
        img.save(io)
        return HttpResponse(io.getvalue(), content_type='image/gif')