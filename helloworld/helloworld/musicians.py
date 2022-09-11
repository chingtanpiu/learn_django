# -*- coding: utf-8 -*-

from django.http import HttpResponse
from ModelMusicians.models import Musicians

# 数据库操作-插入数据
def musicians1(request):
    a = Musicians.objects.create(name='JayChou')
    print(a, type(a))
    return HttpResponse("<p>数据添加成功</p>")

# 数据库操作-查询数据
def musicians2(request):
    # 初始化
    response = ""
    response1 = ""
    response2 = ""
    response3 = ""
    
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Musicians.objects.all()
        
    # filter相当于SQL中的WHERE，可设置条件过滤结果.返回QuerySet 类型数据，类似于 list
    response2 = Musicians.objects.filter(pk=1) # pk是primary key，相当于id，由于id在python是看内存地址的内置函数，因此用pk

    # 查询不符合条件的数据，QuerySet类型数据，类似于 list
    Musicians.objects.exclude(name="ZhouShen")
    
    # 获取单个对象,如果符合筛选条件的对象超过了一个或者没有一个都会抛出错误
    response3 = Musicians.objects.get(pk=1) 
    
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Musicians.objects.order_by('name')[0:2]
    
    #数据排序.返回的是 QuerySet类型数据，类似于list
    Musicians.objects.order_by("id") # 降序为"-id"
    
    # 上面的方法可以连锁使用
    Musicians.objects.filter(name="JayChou").order_by("id")

    
    # 输出所有数据
    for var in list:
        response1 += var.name
    response = response1
    return HttpResponse("<p>" + response + "</p>")


# 数据库操作-更新数据
def musicians3(request):
    # 修改id=1的记录的name字段
    Musicians.objects.filter(id=1).update(name='David Tao')
    # 修改全部记录的name字段
    # Musicians.objects.all().update(name='David Tao')
    return HttpResponse("<p>修改成功</p>")


# 数据库操作-删除数据
def musicians4(request):
    # 删除id=1的数据
    Musicians.objects.filter(id=1).delete()
    # 删除全部记录
    Musicians.objects.all().delete()
    return HttpResponse("<p>删除成功</p>")
