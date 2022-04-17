from django.contrib import admin
from ModelMusicians.models import Musicians, Contact, Tag

# Register your models here.

# 直接激活Musicians, Contact, Tag模型/表
# admin.site.register([Musicians, Contact, Tag])


# 定义了一个ContactAdmin类，用以说明管理页面的自定义格式
class ContactAdmin(admin.ModelAdmin):
    # fields属性定义要显示的字段
    fields = ('name', 'email')

# 由于ContactAdmin类被人为对应为Contact数据模型，我们在注册的时候，需要将它们一起注册
admin.site.register(Contact, ContactAdmin)
admin.site.register([Musicians, Tag])
