# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# 使用POST方法提交表单，并用一个URL和处理函数，同时显示视图和处理请求

# 接受POST的请求数据
@csrf_exempt
def show_and_analysis(request):
    ctx ={}
    if request.POST:
        # POST属性可以返回form表单中所有的键和值
        print("POST属性是个类似于字典的玩意儿:", request.POST)
        # POST属性取某个键的值(返回字符串)，如果该键对应有多个值，取出该键的最后一个值
        ctx['rlt'] = request.POST['query']
        # body的数据类型时二进制流，是原生请求体里的参数内容，在HTTP中用于POST，因为GET没有请求体。处理非HTT 形式的报文时非常有用，例如：二进制图片、XML、Json
        print("原生请求体的内容:", request.body)
        # method属性获取请求的方式
        print("请求方式为:", request.method)
    return render(request, "search_post的模板.html", ctx)
