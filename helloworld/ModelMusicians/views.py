# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from ModelMusicians.models import Musicians

# 数据库操作-删除数据
def musicians(request):
    # 删除id=1的数据
    Musicians.objects.filter(id=2).delete()
    return HttpResponse("<p>删除成功</p>")
