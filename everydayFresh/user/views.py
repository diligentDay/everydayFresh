from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, Http404
from hashlib import sha1
from .models import UserInfo

# Create your views here.


def login(request):
    """登录界面"""
    context = {'title': '登录', 'top': '0'}
    return render(request, 'user/login.html', context)


def register(request):
    """注册页面"""
    context = {'title': '注册', 'top': '0'}
    return render(request, 'user/register.html', context)


def login_handle(request):
    """登录处理逻辑"""
    uname = request.POST.get('user_name')
    upwd = request.POST.get('user_pwd')

    s = sha1()
    s.update(bytes(upwd, 'utf-8'))
    upwd = str(s.hexdigest())

    try:
        user = UserInfo.objects.get(uname=uname)
    except UserInfo.DoesNotExist:
        return redirect('/user/login/')
    if user.upwd == upwd:
        page = request.session.get('last_page')
        request.session['user_id'] = user.id
        request.session['user_name'] = uname
        if page:
            return redirect(page)
        return redirect('/')

    return redirect('/user/login/')


def register_handle(request):
    """注册处理逻辑"""
    uname = request.POST.get('user_name')
    upwd = request.POST.get('user_pwd')
    umail = request.POST.get('user_email')

    s = sha1()
    s.update(bytes(upwd, 'utf-8'))
    upwd = str(s.hexdigest())

    user = UserInfo()
    user.uname = uname
    user.upwd = upwd
    user.umail = umail
    user.ushou = ''
    user.uaddress = ''
    user.ucode = ''
    user.save()
    return redirect('/user/login/')


def register_valid(request):
    """验证用户是否存在"""
    uname = request.GET.get('uname')
    print(uname)
    try:
        UserInfo.objects.get(uname=uname)
    except UserInfo.DoesNotExist:
        return JsonResponse({'valid': 0})
    return JsonResponse({'valid': 1})


def center(request):
    context = {'title': '用户中心'}

    return render(request, 'user/center.html', context)


def site(request):
    context = {'title': '用户中心'}

    return render(request, 'user/site.html', context)


def order(request):
    context = {'title': '用户中心'}

    return render(request, 'user/order.html', context)

