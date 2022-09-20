# 姓名：刘超
# 开发时间：2022/6/28 16:07
# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from my_app import models
from my_app.utils.pagination import Pagination
from django import forms
from my_app.utils.bootstrap import BootStrapForm
from my_app.utils.encrypt import md5
from my_app.utils.img_code import check_code
# 生成验证码时用
from io import BytesIO
import os

class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True    # 必填
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),   # render_value=True表示密码输入后不会置空
        required=True    # 必填
    )
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True  # 必填
    )

    def clean_password(self):
        pwd_md5 = md5(self.cleaned_data.get("password"))
        return pwd_md5


# class LoginModelForm(forms.ModelForm):
#     class Meta:
#         model = models.Admin
#         labels = ["username","password"]

def login(request):
    req_method = request.method
    if req_method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {"form": form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证成功，获取到的用户名和密码
        # print(form.cleaned_data)   # {'username': 'root', 'password': '4876931d2563f86d7abfa501e3a51554','code': 'YLCHV'}

        # 验证码的校验
        # pop('code')相当于删除cleaned_data字典中的code字段，
        # 删除是因为filter(**form.cleaned_data).first()数据库中没有code字段
        user_input_code = form.cleaned_data.pop('code')
        img_code = request.session.get('image_code',"")
        if user_input_code.upper() != img_code.upper():
            form.add_error("code", "验证码错误")  # form.add_error主动添加一个错误
            return render(request, 'login.html', {"form": form})

        # 去数据库校验用户名和密码是否正确，获取用户对象、没有数据为None
        # admin = models.Admin.objects.filter(username="xxx",password="xxx").first()
        admin = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin:  # 说明用户名和密码不存在
            # form.add_error("username", "用户名或密码错误")
            form.add_error("password","用户名或密码错误")     # form.add_error主动添加一个错误
            return render(request, 'login.html', {"form": form})

        # 用户名和密码正确
        # 网站生成随机字符串; 写到用户浏览器的cookie中；再写入到session中；
        request.session["info"] = {'id': admin.id, 'username': admin.username, "name": admin.name,'role': admin.get_role_display()}
        # session可以保存7天
        request.session.set_expiry(60 * 60 * 24 * 7)

        # return redirect("/yibiao/list/")
        return redirect("/")
    return render(request, 'login.html', {"form": form})

def logout(request):
    '''注销'''
    request.session.clear()
    return redirect("/login/")


def image_code(request):
    '''生成图像验证码'''

    os.chdir('E:\python\django_yibiao')  # 改变工作目录

    # 调用pillow函数，生成图片
    img,code_string = check_code()
    # print(code_string)  # YLCHV 每次都会变

    # 写入到自己的session中（以便于后续获取验证码再进行校验）
    request.session['image_code'] = code_string
    # 给session设置60s超时
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream,'png')
    return HttpResponse(stream.getvalue())
