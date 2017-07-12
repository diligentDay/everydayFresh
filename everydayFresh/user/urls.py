# coding:utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.center),
    url(r'^site/$', views.site),
    url(r'^order/$', views.order),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^login_handle/$', views.login_handle),
    url(r'^register_handle', views.register_handle),
    url(r'^register_valid/$', views.register_valid),

]