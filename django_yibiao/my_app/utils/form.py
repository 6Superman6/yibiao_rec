# 姓名：刘超
# 开发时间：2022/6/21 16:09
# -*- coding: utf-8 -*-

from my_app import models
from django import forms
import re
# 导入正则表达式的包
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from my_app.utils.pagination import Pagination
from my_app.utils.bootstrap import BootStrapModelForm
from my_app.utils.encrypt import md5

'''管理员ModelForm'''


class AdminModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)  # render_value=True，输入之后内容不会置空
    )

    class Meta:
        model = models.Admin
        fields = ["username","password","confirm_password","name","age","gender","mobile", "role"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)  # render_value=True，输入之后内容不会置空
        }

    # 判断用户名是否已经存在
    def clean_username(self):  # 第一执行
        txt_username = self.cleaned_data["username"]
        # 判断用户名是否已经存在
        exists = models.Admin.objects.filter(username=txt_username).exists()
        if exists:
            raise ValidationError("用户名已存在")
        return txt_username

    # 数据验证：验证手机号
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]

        if len(txt_mobile) != 11:
            # 验证不通过
            raise ValidationError("格式错误")
        # 判断数据库中的手机号是否存在
        exists = models.Admin.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")

        if re.match(r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$', txt_mobile):
            return txt_mobile  # 验证通过,用户输入的值返回
        else:
            raise forms.ValidationError(u"手机号码非法", code='mobile invalid')

    def clean_password(self):  # 第二执行
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):  # 第三执行
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if pwd != confirm:
            raise ValidationError("密码不一致")
        # 返回什么，此字段以后保存到数据库就是什么。
        return confirm

class UserModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)  # render_value=True，输入之后内容不会置空
    )

    class Meta:
        model = models.Admin
        fields = ["username","password","confirm_password","name","age","gender","mobile"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)  # render_value=True，输入之后内容不会置空
        }

    # 判断用户名是否已经存在
    def clean_username(self):  # 第一执行
        txt_username = self.cleaned_data["username"]
        # 判断用户名是否已经存在
        exists = models.Admin.objects.filter(username=txt_username).exists()
        if exists:
            raise ValidationError("用户名已存在")
        return txt_username

    # 数据验证：验证手机号
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]

        if len(txt_mobile) != 11:
            # 验证不通过
            raise ValidationError("格式错误")
        # 判断数据库中的手机号是否存在
        exists = models.Admin.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")

        if re.match(r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$', txt_mobile):
            return txt_mobile  # 验证通过,用户输入的值返回
        else:
            raise forms.ValidationError(u"手机号码非法", code='mobile invalid')

    def clean_password(self):  # 第二执行
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):  # 第三执行
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if pwd != confirm:
            raise ValidationError("密码不一致")
        # 返回什么，此字段以后保存到数据库就是什么。
        return confirm

class AdminEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ["username", "name","age","gender","mobile", "role"]

    # 判断用户名是否已经存在
    def clean_username(self):
        txt_username = self.cleaned_data["username"]
        # models.Admin.objects.exclude(id=aid)  排除id=pid的所有数据
        aid = self.instance.pk  # 获取编辑的那一行数据的id
        # 判断数据库中的用户名是否存在(除了自己的用户名)
        exists = models.Admin.objects.exclude(id=aid).filter(username=txt_username).exists()
        if exists:
            raise ValidationError("用户名已存在")
        return txt_username

    # 数据验证：验证手机号
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]

        if len(txt_mobile) != 11:
            # 验证不通过
            raise ValidationError("格式错误")

        # models.Admin.objects.exclude(id=pid)  排除id=pid的所有数据
        pid = self.instance.pk  # 获取编辑的那一行数据的id
        # 判断数据库中的手机号是否存在(除了自己的手机号)
        exists = models.Admin.objects.exclude(id=pid).filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")

        if re.match(r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$', txt_mobile):
            return txt_mobile  # 验证通过,用户输入的值返回
        else:
            raise forms.ValidationError(u"手机号码非法", code='mobile invalid')

class UserEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ["username", "name","age","gender","mobile"]

    # 判断用户名是否已经存在
    def clean_username(self):
        txt_username = self.cleaned_data["username"]
        # models.Admin.objects.exclude(id=aid)  排除id=pid的所有数据
        aid = self.instance.pk  # 获取编辑的那一行数据的id
        # 判断数据库中的用户名是否存在(除了自己的用户名)
        exists = models.Admin.objects.exclude(id=aid).filter(username=txt_username).exists()
        if exists:
            raise ValidationError("用户名已存在")
        return txt_username

    # 数据验证：验证手机号
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]

        if len(txt_mobile) != 11:
            # 验证不通过
            raise ValidationError("格式错误")

        # models.Admin.objects.exclude(id=pid)  排除id=pid的所有数据
        pid = self.instance.pk  # 获取编辑的那一行数据的id
        # 判断数据库中的手机号是否存在(除了自己的手机号)
        exists = models.Admin.objects.exclude(id=pid).filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")

        if re.match(r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$', txt_mobile):
            return txt_mobile  # 验证通过,用户输入的值返回
        else:
            raise forms.ValidationError(u"手机号码非法", code='mobile invalid')


class AdminResetModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ['password', 'confirm_password']
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):  # 第一执行
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)

        # 去数据库校验当前密码和新输入的密码是否一致
        exists = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError("不能与以前的密码相同")

        return md5_pwd

    def clean_confirm_password(self):  # 第二执行
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回什么，此字段以后保存到数据库就是什么。
        return confirm
