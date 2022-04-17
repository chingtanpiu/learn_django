from django.contrib import admin
from ModelMusicians.models import Musicians, Contact, Tag

# Register your models here.

# 直接激活Musicians, Contact, Tag模型/表
# admin.site.register([Musicians, Contact, Tag])


# 定义了一个ContactAdmin类，用以说明管理页面的自定义格式
class ContactAdmin(admin.ModelAdmin):
    # fields属性定义要显示ModelMusicians_Contact表的哪些字段
    fields = ('name', 'email')

# 由于我们想把ContactAdmin类定义的格式针对Contact数据模型（即ModelMusicians_Contact表）使用，因此我们在注册的时候，需要将ContactAdmin类和Contact一起注册
admin.site.register(Contact, ContactAdmin)
# 将多个模型/表注册进admin系统。这种注册方式就没有自定义的管理模型
admin.site.register([Musicians, Tag])
