from django.db import models
from django.utils.timezone import now
import datetime
import django

# Create your models here.

class Admin(models.Model):
    '''用户'''
    username = models.CharField(verbose_name="用户名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)

    role_choices = (
        (1,"用户"),
        (2,"管理员")
    )
    role = models.SmallIntegerField(verbose_name="角色",choices=role_choices,default=1)

    name = models.CharField(verbose_name="姓名", max_length=16)
    age = models.IntegerField(verbose_name="年龄")
    # 在django中做的约束
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    mobile = models.CharField(verbose_name="手机号", max_length=32)
    create_time = models.DateField(verbose_name="创建时间",default=now)



    def __str__(self):  # 输出对象时显示username
        return self.username

class Yibiao(models.Model):
    '''仪表信息表'''
    # 本质上数据库也是CharField，会自动保存数据。  upload_to='img_test_2/' 表示文件会自动保存在yibiao_ocr目录下的img_test_2目录中
    img = models.FileField(verbose_name="仪表图片", max_length=128, upload_to='img_test_2/')

    # img_result decimal(10,2) 小数
    img_result = models.DecimalField(verbose_name="识别结果",max_digits=10,decimal_places=2,default=0)

    img_name = models.CharField(verbose_name="图片名称",max_length=128)

    # 会在数据库表中自动创建admin_id字段
    admin = models.ForeignKey(verbose_name="用户", to="Admin", to_field="id", on_delete=models.CASCADE)

class Imgtemplate(models.Model):
    '''模板信息表'''
    name = models.CharField(verbose_name="模板名称",max_length=128)

    '''模板参数信息'''
    c_x = models.DecimalField(verbose_name="圆心x像素坐标",max_digits=10,decimal_places=2,default=0)
    c_y = models.DecimalField(verbose_name="圆心y像素坐标",max_digits=10,decimal_places=2,default=0)
    a = models.CharField(verbose_name="刻度及其对应像素坐标",max_length=256)
    maxd = models.DecimalField(verbose_name="最大刻度值", max_digits=10,decimal_places=2,default=0)
    fir_d = models.DecimalField(verbose_name="配置0刻度线参数1", max_digits=10,decimal_places=2,default=0)
    sec_d = models.DecimalField(verbose_name="配置0刻度线参数2", max_digits=10,decimal_places=2,default=0)
    scale = models.DecimalField(verbose_name="刻度间隔", max_digits=10,decimal_places=2,default=0)
    img_template = models.FileField(verbose_name="模板图片", max_length=128, upload_to='TemplateLib/')

class ImgOcrRec(models.Model):
    '''ocr文字识别表'''
    img = models.FileField(verbose_name="识别图片", max_length=128, upload_to='rec/')

    img_result = models.TextField(verbose_name="识别结果")

    # 会在数据库表中自动创建admin_id字段
    admin = models.ForeignKey(verbose_name="用户", to="Admin", to_field="id", on_delete=models.CASCADE)

class WellDanger(models.Model):
    '''小盖板检测'''
    imgrec = models.FileField(verbose_name="识别图片", max_length=128, upload_to='yolov5_master/number/')

    imgresult = models.CharField(verbose_name="识别结果",max_length=128)

    # 会在数据库表中自动创建admin_id字段
    admin = models.ForeignKey(verbose_name="用户", to="Admin", to_field="id", on_delete=models.CASCADE)



