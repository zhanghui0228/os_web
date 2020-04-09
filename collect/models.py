from django.db import models

# Create your models here.


class Web(models.Model):
    ''' os web系统的web表信息 '''
    name = models.CharField('监控项名称', max_length=64)
    value = models.CharField('监控项值', max_length=64)
    create_time = models.DateTimeField('创建时间', auto_now_add=True, null=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'os_web'