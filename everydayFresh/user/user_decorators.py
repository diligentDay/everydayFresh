# coding:utf-8
from django.shortcuts import redirect


def user_login(func):
    def func1(request, *args, **kwargs):
        if request.session.get('uid') is None:
            return redirect(request, '/user/login/')
        else:
            return func(request, *args, **kwargs)
    return func1