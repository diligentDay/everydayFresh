# coding: utf-8
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


# Create your views here.
def index(request):
    context = {'title': '首页'}
    context['glist'] = []
    for i in range(1, 7):
        gtype = models.TypeInfo.objects.get(id=i)
        new_list = gtype.goodsinfo_set.all().order_by('-id')[:4]
        goods_list = gtype.goodsinfo_set.all().order_by('-gprice')[:4]
        context['glist'].append({'t1': gtype, 'clist': new_list, 'nlist': goods_list})
    return render(request, 'goods/index.html', context)


def detail(request, gid):
    context = {'title': '商品详情页'}
    context['goods'] = models.GoodsInfo.objects.get(id=gid)
    context['new_list'] = models.GoodsInfo.objects.order_by('-id')[:3]
    return render(request, 'goods/detail.html', context)


def list_goods(request, tid, pindex, order_by):
    context = {'title': '商品列表', 'order_by': order_by}
    context['t1'] = models.TypeInfo.objects.get(id=tid)
    desc = 1
    if order_by == '2':
        desc = request.GET.get('desc', '1')
        if desc == '1':
            goods_list = context['t1'].goodsinfo_set.order_by('-gprice')
        else:
            goods_list = context['t1'].goodsinfo_set.order_by('gprice')

    elif order_by == '3':
        goods_list = context['t1'].goodsinfo_set.order_by('-gclick')
    else:
        goods_list = context['t1'].goodsinfo_set.order_by('-id')

    paginator = Paginator(goods_list, 6)
    pindex = int(pindex)
    context['page'] = paginator.page(pindex)
    if paginator.num_pages <= 5:
        context['page_range'] = range(1, paginator.num_pages+1)
    else:
        if pindex <= 2:
            context['page_range'] = range(1, 6)
        elif pindex >= paginator.num_pages-1:
            context['page_range'] = paginator.page_range[-5:]
        else:
            context['page_range'] = range(pindex-2, pindex+3)
    context['desc'] = desc
    context['orderby'] = order_by
    context['tid'] = tid
    context['pindex'] = pindex

    return render(request, 'goods/list.html', context)


