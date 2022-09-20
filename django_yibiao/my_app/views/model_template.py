# 姓名：刘超
# 开发时间：2022/7/15 10:14
# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse,redirect
from my_app.utils.pagination import Pagination
from my_app import models
from my_app.utils.bootstrap import BootStrapModelForm
from django import forms
from django.http import JsonResponse

from yibiao_ocr.model_type3 import make_model_template

# 免除post请求的csrf认证
from django.views.decorators.csrf import csrf_exempt

import os
import glob

class TemplateModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ["img_template"]  # 排除不想添加样式的字段

    class Meta:
        model = models.Imgtemplate
        exclude = ["name"]

def model_list(request):
    '''仪表模板图像列表'''
    queryset = models.Imgtemplate.objects.all().order_by("-id")

    page_object = Pagination(request, queryset, page_size=5)  # 每页5个数据
    form = TemplateModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }
    return render(request, 'imgTemplate.html', context)

@csrf_exempt
def model_add(request):
    '''添加模板图片'''

    Img = request.FILES.get("img_template")
    if Img:
        img_name = request.FILES.get("img_template").name
        exists = models.Imgtemplate.objects.filter(name=img_name).exists()
        if exists:
            return JsonResponse({"status": False, "msg": "请误上传同名或者相同的模板"})

    form = TemplateModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():

        form.save()
        yid = form.instance.id
        name = str(form.instance.img_template).split('/')[-1]
        models.Imgtemplate.objects.filter(id=yid).update(name=name)
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})

def model_del(request):
    '''删除模板'''
    tid = request.GET.get("uid")
    Template = models.Imgtemplate.objects.filter(id=tid).first()
    if not Template:
        return JsonResponse({"status": False, "error": "删除失败，数据不存在"})

    template_name = str(Template.img_template)  # TemplateLib/code.png
    # print(img_name)  # img_test_2/001_bwajbah.jpg
    # print(os.getcwd())  # E:\python\django_yibiao
    os.chdir('E:\python\django_yibiao')  # 改变工作目录
    paths = glob.glob(os.path.join('yibiao_ocr', template_name))
    # 删除名称为img_name图像
    for file in paths:
        # print(file)   # yibiao_ocr/TemplateLib/code.png
        os.remove(file)

    models.Imgtemplate.objects.filter(id=tid).delete()
    return JsonResponse({"status": True})

def model_detail(request):
    '''模板详情'''
    uid = request.GET.get("uid")
    # values("title","price","status") 获取一个字典：{"title": "123","price": 36,"status": 1}
    Template_dict = models.Imgtemplate.objects.filter(id=uid).values("c_x","c_y","a","maxd","fir_d","sec_d","scale","img_template").first()
    # print(Template_dict) # {'c_x': Decimal('23.00'), 'c_y': Decimal('56.00'), 'a': '{0.0: (61.5, 152.5), 0.1: (50.5, 109.5), 0.2: (77.5, 64.0), 0.3: (126.0, 46.0), 0.4: (169.0, 70.0), 0.5: (188.5, 122.0), 0.6: (164.0, 168.5)}', 'maxd': Decimal('0.60'), 'fir_d': Decimal('0.50'), 'sec_d': Decimal('0.60'), 'scale': Decimal('0.10'), 'img_template': 'TemplateLib/002_M2MuHYm.jpg'}
    img_name = Template_dict["img_template"]
    # print(img_name)  # TemplateLib/002_M2MuHYm.jpg
    if not Template_dict:
        return JsonResponse({"status": False, "error": "数据不存在，请刷新重试"})

    result = {
        "status": True,
        "img_name": img_name,
        "data": Template_dict
    }
    return JsonResponse(result)

@csrf_exempt
def model_edit(request):
    '''编辑模板图片'''
    uid = request.GET.get("uid")
    Template = models.Imgtemplate.objects.filter(id=uid).first()
    if not Template:
        return JsonResponse({"status": False, "error": "数据不存在，请刷新重试"})
    form = TemplateModelForm(data=request.POST,instance=Template)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})

def make_template_msg(request):
    '''用ocr识别模板信息，生成模板库信息'''
    try:
        make_model_template()
        return JsonResponse({"status": True})
    except Exception as e:
        return JsonResponse({"status": False,"msg": "生成失败，数据异常"})



