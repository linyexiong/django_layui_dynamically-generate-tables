from django.db import models

# Create your models here.


# 用户信息表 tbl_user_info
class UserInfo(models.Model):
    username = models.CharField('用户名', max_length=30, null=True)  # 用户名
    age = models.IntegerField('年龄', null=True)  # 年龄
    sex = models.CharField('性别', max_length=1, null=True)  # 性别，男或女
    mobile = models.CharField('手机号码', max_length=30, null=True)  # 手机号码
    address = models.CharField('地址', max_length=150, null=True)  # 地址
    createtime = models.DateTimeField('创建时间', auto_now_add=True, null=True)  # 创建时间

    class Meta:
        app_label = 'user'
        db_table = 'tbl_user_info'
        verbose_name = '用户信息表'    # admin后台显示的名称
        verbose_name_plural = verbose_name