# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'Classes.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
