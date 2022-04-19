from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
 
def hello(request):
    # HttpResponse对象之HttpResponse()返回文本，参数为字符串(可以带html标签)
    return HttpResponse("views的hello视图函数") 
    # 字符串(可以带html标签)
    # return HttpResponse("<a href='https://www.runoob.com/'>菜鸟教程</a>")

def runoob1(request):
    a = {}
    a['hello'] = 'runoob视图函数' 
    # HttpResponse对象之render()
    return render(request, 'views的模板.html', a) # a字典{"hello":"runoob视图函数"}的hello键值可在模板中的用变量{{ hello }}调用

# 添加require_http_methode装饰器来显示请求方式，但是浏览器默认就是发GET：要么用postman之类的，要么直接在模板中将浏览器的GET请求转为POST(参见post.html/get.html)而无需再用此装饰器
# @require_http_methods(["POST"]) 
def runoob(request):
    view_param = 0
    view_lpbn = [("黑色柳丁","颗粒无收"), ("Unbelievable","最佳制作人"), ("叶惠美","最佳专辑")]
    musician_list = {'JayChou', 'David Tao', 'LeehomWang'}
    link = "<a href='http://nas.vainglory.buzz:18080/'>qbittorrent</a>"
    # path属性用户获取请求URL中的路径部分
    print("路径部分为:", request.path)
    # 利用render()返回一个页面
    return render(request, 'views的模板.html', {"tem_param": view_param, "tem_lpbn": view_lpbn, "link": link, "musician_list": musician_list})