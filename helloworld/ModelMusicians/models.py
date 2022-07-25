from turtle import mode
from django.db import models


"""
数据库模型一般写在models.py文件中，然后python3 manage.py makemigrations，第一次执行该操作会在app下面创建migrations目录，并创建记录了当前的建表、依赖等信息的0001_inital.py文件。
下一次执行该操作时，如果有关于model.py改动，会在migrations下生成已修改内容为名，类似0002_alter_permission_name_max_length.py的文件，
文件中记录了你修改字段等信息。如果没有改动则提示：No changes detected。
需要注意的是，makemigrations并不会将这些改动真正执行、迁移到数据库中！执行Python manage.py migrate后，就会把修改应用到数据库中
"""



# 在这里通过创建类来构建ORM模型。类名代表数据库表名（默认最终表名有appname前缀，为ModelMusicians_musicians;库名则是服务器配置数据库是创建的djmm， ORM无法操作到库级别，只能操作到数据表），且继承了models.Model
# 类里面的字段代表数据表中的字段(name)，数据类型则由CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度
class Musicians(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.IntegerField(max_length=3, verbose_name='年龄')
    sex = models.CharField()
    def __unicode__(self):
        return self.name

    # Meta详见https://www.cnblogs.com/tongchengbin/p/7670927.html
    class Meta:
        db_table = 'musicians_info' # 自定义数据库表名
        verbose_name = "音乐人信息" # 给你的模型类起一个更可读的名字
        verbose_name_plural = verbose_name

class Contact(models.Model):
    name   = models.CharField(max_length=200, verbose_name='姓名')
    # IntegerField储存整数
    age    = models.IntegerField(default=0, verbose_name='年龄')
    # EmailField储存邮件
    email  = models.EmailField()
    def __unicode__(self):
        return self.name
 
class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,)
    name    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name