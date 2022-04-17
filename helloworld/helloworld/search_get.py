from django.http import HttpResponse
from django.shortcuts import render

# GET方法提交表单的话，视图显示和请求处理分成两个函数处理。

# 表单视图显示函数
def show_form(request):
    # 返回一个页面，相应的要在templates目录下加get.html文件
    return render(request, 'get.html') 

# 处理请求数据(返回响应)
def analysis_form(request):
    request.encoding = 'utf-8'
    # GET属性可以返回GET请求中的全部键和值
    print("GET属性可以返回GET请求中的全部键和值：", request.GET)
    # GET属性取某个键的值(返回字符串)，如果该键对应有多个值，取出该键的最后一个值
    if 'query' in request.GET and request.GET['query']:
        message = '你搜索的内容为:'+request.GET['query']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)