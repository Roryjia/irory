# -*-coding:utf-8 -*-
#
# Created on 2016-04-01
#      __      __
#  -  /__) _  /__) __/
#  / / (  (/ / (    /
#                  /

from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Blog


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget)

    class Meta:
        models = Blog
        fields = ('cate', 'tags', 'name', 'content', 'pv', 'is_top', 'is_active', 'is_deleted')
