# Generated by Django 4.0 on 2022-02-08 15:14

from django.db import migrations, models

# 这里的东西应该是migrate命令根据models.py文件生成的，而不是手写的
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musicians',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('age', models.IntegerField(max_length=3, verbose_name='年龄')),
                ('sex', models.CharField()),
            ],
        ),
    ]
