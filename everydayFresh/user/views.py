from django.shortcuts import render

# Create your views here.


def login(request):
    """登录界面"""
    context = {'title': '登录'}
    return render(request, 'user/login.html', context)


def register(request):
    """注册页面"""
    context = {'title': '注册'}
    return render(request, 'user/register', context)


def login_handle(request):
    """登录处理逻辑"""


def register_handle(request):
    """注册处理逻辑"""
