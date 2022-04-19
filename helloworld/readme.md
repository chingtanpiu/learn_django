└── helloworld
    ├── helloworld
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── musicians.py:供urls.py调用。对某个表进行操作。
    │   ├── search_get.py:供urls.py调用。解析get请求，提取请求数据进行处理并返回
    │   ├── search_post.py:供urls.py调用。解析post请求，提取请求数据进行处理并返回
    │   ├── settings.py:对数据库、app的配置。配置DB时，NAME是datebase的名字(类似basketball_yc_db1这样的，而不是‘篮球压测服’),而且ENGINE配置'mysql'。
    │   ├── urls.py：运用url()、path()——django4.0中用re_path()兼容此二者，将route与客户端请求路径匹配后，调用views.py中的视图函数或其它py文件的函数(不在helloworld目录也行，只要把文件在urls.py中import)
    │   ├── views.py：供urls.py调用。views.py用HttpResponse()返回简单的文本，用render(request, 'templates目录下的模板.html', {'模板变量1'：'views变量1', '模板变量2'：'views变量2'})返回预制模板的样式。views.py可以向模板传列表，想必其它py也能。
    │   └── wsgi.py
    ├── manage.py
    ├── ModelMusicians：django模型使用自带的ORM，使用模型首先要创建一个app，django-admin startapp ModelMusicians(app的名字),然后会产生一个模型目录/helloworld/ModelMusicians，在目录的models.py文件中通过创建类(也就是创建模型)来设计表，之后就是构建表结构了(见‘构建表结构’)，构建之后构建信息在migrations目录内。
    │   ├── admin.py：自定义某张表/模型(models.py中定义的类)的管理页面格式。admin工具的激活和访问地址见urls.py文件。可以用python manage.py createsuperuser来创建超级用户登录admin系统。
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   └── __init__.py  
    │   ├── models.py：通过创建类来构建表结构。
    │   ├── tests.py
    │   └── views.py
    ├── readme.md
    └── templates：模板目录，放置(类)视图函数文件的模板
        ├── search_get模板.html
        ├── search_post的模板.html
        └── views的模板.html
        


创建项目:django-admin startproject helloworld:会创建helloworld项目目录，目录下还有个helloworld的，还有templates目录。



尚待深入：模板中对数据的处理(大小写、显示参数的前几位)、for语句、{% empty %}从句、ifequal/ifnotequal标签、注释标签等；自定义tag和filter；csrf_token



ORM:ORM将python的代码转化为SQL，SLQ通过pymysql传到DB服务器，务器执行SQL并返回结果。


‘配置mysql数据库连接信息’:
1.修改settings.py文件中的DATABASES配置项
2.在与settings.py同级目录下的__init__.py中引入pymysql模块并进行设置


‘构建表结构’：
1.在settings.py中找到INSTALLED_APPS这一项，添加app名如ModelMusicians
2.python3 manage.py migrate   # 创建表结构
3.python3 manage.py makemigrations ModelMusicians  # 让 Django 知道我们在我们的模型有一些变更
4.python3 manage.py migrate ModelMusicians   # 创建表结构
5.构建信息在migrations目录内