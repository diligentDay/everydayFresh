from django.shortcuts import render, redirect
from .models import *
from hashlib import sha1

# Create your views here.

def register(request):
    context = {'title': '注册', }

    return render(request, 'user/register.html', context)


def login(request):
    context = {'title': '登陆', }

    return render(request, 'user/login.html', context)


def register_handle(request):
    # 接收数据
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    umail = post.get('user_email')
    # 加密
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()
    # 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd_sha1
    user.umail = umail
    user.save()
    # 完成转向
    return redirect('/user/login/')

