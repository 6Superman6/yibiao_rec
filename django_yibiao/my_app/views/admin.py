# 姓名：刘超
# 开发时间：2022/6/27 15:38
# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse, redirect
# from my_app.models import Department,UserInfo
from my_app import models
from my_app.utils.pagination import Pagination
from my_app.utils.form import AdminModelForm,AdminEditModelForm,AdminResetModelForm,UserModelForm,UserEditModelForm
from django.http import JsonResponse
# 免除post请求的csrf认证
from django.views.decorators.csrf import csrf_exempt
'''管理员接口'''

# 管理员列表
def admin_list(request):

    # admin = request.session.get("info")
    # admin = request.session["info"]
    # print(admin["id"])   # 8
    # print(admin["name"]) # root

    # 搜索
    data_dict = {}
    # 第二个值为默认值
    # search_data对用户名进行模糊查询
    search_data = request.GET.get("q","")  # search_data在没传入q值的时候为空
    if search_data: # search_data值不为空时
        data_dict['username__contains'] = search_data

    admin_list = models.Admin.objects.filter(**data_dict)
    # print(admin_list)

    # 页码组件类
    page_object = Pagination(request,admin_list,page_size=2)  # 每页最多显示2个数据

    render_data ={
        "search_data": search_data,
        "admin_list": page_object.page_queryset,  # 获取起止页所需数据
        "page_string": page_object.html()  # 页码所需要的html代码
    }

    return render(request, 'admin_list.html',render_data)

from django import forms
from django.core.exceptions import ValidationError
from my_app.utils.bootstrap import BootStrapModelForm




# 添加管理员
def admin_add(request):
    title = "新建管理员"
    req_method = request.method
    if req_method == 'GET':
        form = AdminModelForm()
        return render(request, 'public_xxx_add.html', {"title": title, "form": form})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():  # 数据验证成功
        # print(form.cleaned_data)  # {'username': 'ttt', 'password': '122', 'confirm_password': '123'}
        form.save()
        return redirect("/admin/list/")
    return render(request, 'public_xxx_add.html', {"title": title, "form": form})

# 更新管理员
def admin_edit(request,aid):
    title = "更新管理员"
    admin = models.Admin.objects.filter(id=aid).first()
    if not admin:
        # return render(request,'error.html',{"msg": "数据不存在"})
        return redirect("/admin/list/")
    req_method = request.method
    if req_method == 'GET':
        form = AdminEditModelForm(instance=admin)
        return render(request, 'public_xxx_add.html', {"title": title,"form": form})
    form = AdminEditModelForm(data=request.POST,instance=admin)
    if form.is_valid():
        # 因为AdminEditModelForm中只定义了username这一个字段，所以更新时只会更新这一个值
        form.save()
        return redirect("/admin/list/")
    return render(request, 'public_xxx_add.html', {"title": title,"form": form})

# 删除管理员
def admin_del(request):
    aid = request.GET.get("id")
    admin = models.Admin.objects.filter(id=aid).first()
    if not admin:
        return render(request,'error.html',{"msg": "数据不存在"})
        # return redirect("/admin/list/")
    models.Admin.objects.filter(id=aid).delete()
    return redirect("/admin/list/")

# 重置密码
def admin_reset(request,aid):
    admin = models.Admin.objects.filter(id=aid).first()
    if not admin:
        # return render(request, 'error.html', {"msg": "数据不存在"})
        return redirect("/admin/list/")
    title = "重置密码 - {}".format(admin.username)
    req_method = request.method
    if req_method == 'GET':
        # form = AdminResetModelForm(instance=admin)      # 更新密码
        form = AdminResetModelForm()      #重置密码不让她看到原来的密码，让其显示为空
        return render(request, 'public_xxx_add.html', {"title": title,"form": form})
    form = AdminResetModelForm(data=request.POST,instance=admin)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")
    return render(request, 'public_xxx_add.html', {"title": title, "form": form})

# 用户注册
@csrf_exempt
def user_add(request):
    title = "用户注册"
    req_method = request.method
    if req_method == 'GET':
        form = UserModelForm()
        return render(request, 'register.html', {"title": title, "form": form})
    form = UserModelForm(data=request.POST)
    print(request.POST)
    if form.is_valid():  # 数据验证成功
        # print(form.cleaned_data)  # {'username': 'ttt', 'password': '122', 'confirm_password': '123'}
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})

# 更新用户
def user_edit(request,aid):
    # print('更新用户: ',request.method)
    admin = models.Admin.objects.filter(id=aid).first()
    if not admin:
        # return render(request,'error.html',{"msg": "数据不存在"})
        return JsonResponse({"status": False, "msg": "数据不存在，请刷新重试"})
    title = "个人资料 - {}".format(admin.name)
    req_method = request.method
    if req_method == 'GET':
        form = UserEditModelForm(instance=admin)
        return render(request, 'my_message.html', {"title": title,"form": form})
    form = UserEditModelForm(data=request.POST,instance=admin)
    # print('form: ',form)
    if form.is_valid():
        # 因为AdminEditModelForm中只定义了username这一个字段，所以更新时只会更新这一个值
        form.save()
        request.session["info"] = {'id': admin.id, 'username': form.instance.username, "name": form.instance.name,'role': admin.get_role_display()}
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})

# 用户重置密码
def user_reset(request,aid):
    admin = models.Admin.objects.filter(id=aid).first()
    if not admin:
        # return render(request, 'error.html', {"msg": "数据不存在"})
        # return redirect("/yibiao/list/")
        return redirect("/")
    title = "重置密码 - {}".format(admin.username)
    req_method = request.method
    if req_method == 'GET':
        # form = AdminResetModelForm(instance=admin)      # 更新密码
        form = AdminResetModelForm()      #重置密码不让她看到原来的密码，让其显示为空
        return render(request, 'public_xxx_add.html', {"title": title,"form": form})
    form = AdminResetModelForm(data=request.POST,instance=admin)
    if form.is_valid():
        form.save()
        return redirect("/")
        # return redirect("/yibiao/list/")
    return render(request, 'public_xxx_add.html', {"title": title, "form": form})