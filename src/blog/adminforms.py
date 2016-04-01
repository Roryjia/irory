# -*-coding:utf-8 -*-
# 
# Copyright (C) 2012-2015 Lianbi TECH Co., Ltd. All rights reserved.
# Created on 2015-07-02, by rory
# 
# 

__author__ = 'rory'

from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Blog


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget)

    class Meta:
        models = Blog
        fields = ('cate', 'tags', 'name', 'content', 'pv', 'is_top', 'is_active', 'is_deleted')
