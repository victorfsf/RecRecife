# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url
from recmap import views

urlpatterns = patterns('',
                       url(r'^$', views.view_teste, name='teste'),
                       )
