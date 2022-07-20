from turtle import mode
from django.db import models


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