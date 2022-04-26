"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import search_get, views, musicians, search_post
from django.urls import path, re_path, include


# 默认的配置
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# 绑定URL与视图函数hello()
# 4.0中使用re_path()方法兼容url()方法和path()
# django将route与客户请求的路径相匹配
# urlpatterns = [
#     re_path(r'^$', views.hello),
#     re_path('换个不是hello的路由(路径)也行', views.hello)
# ]

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path('runoob/', views.runoob),
    re_path('musicians/', musicians.musicians4),
    re_path('ModelMusicians_appname/', include("ModelMusicians.urls")),
    re_path(r'^search_get/$', search_get.show_form),
    re_path(r'^search/$', search_get.analysis_form),
    re_path(R'^search_post/$', search_post.show_and_analysis)
]


