# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Musicians
import json

# 数据库操作-删除数据
def musicians_delete(request):
    # 删除id=1的数据
    Musicians.objects.filter(id=2).delete()
    return HttpResponse("<p>删除成功</p>")

# 数据库操作查询数据
def musicians_query(request):
    msg = {"msg": "success"}
    # user_id = request.session.get('_auth_user_id') # 获取请求中的session信息，这里用不到
    params = json.loads(request.body) # 获取收到的请求中的请求体，并json化
    name = params.get("query", None) # 从json中获取query字段
    try:
        musician_info = Musicians.objects.get(name=name) # 查询数据库中是否有此人
        return musician_info # 这里不清楚这样返回的是什么
    except:
        msg["msg"] = "查无此人"

    return JsonResponse(data=msg)