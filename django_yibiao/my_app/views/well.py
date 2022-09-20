# 姓名：刘超
# 开发时间：2022/7/19 15:05
# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse,redirect
from my_app.utils.pagination import Pagination
from my_app import models
from my_app.utils.bootstrap import BootStrapModelForm
from django import forms
from django.http import JsonResponse
from yibiao_ocr.yolov5_master.detect2 import detect

import os
import glob

# 免除post请求的csrf认证
from django.views.decorators.csrf import csrf_exempt

'''图片上传的ModelForm'''
class WellModelForm(BootStrapModelForm):

    bootstrap_exclude_fields = ["imgrec"]  # 排除不想添加样式的字段

    class Meta:
        model = models.WellDanger
        exclude = ["imgresult", "admin"]  # 排除img_result和admin后的所有属性（排除订单号和所属用户）
        widgets = {
            "imgrec": forms.FileInput(attrs={"accept": "image/*"}),
            # 限制input file上传类型只能是图片: <input type="file" accept="image/*">
        }

'''小盖板识别'''
def well(request):
    form = WellModelForm()
    return render(request,'well.html',{"form": form})

'''检测识别'''
@csrf_exempt
def well_rec(request):
    form = WellModelForm(data=request.POST, files=request.FILES)

    try:
        if form.is_valid():
            # 固定设置管理员ID，去哪里获取？(当前登录用户的id)
            form.instance.admin_id = request.session["info"]["id"]
            form.save()
            yid = form.instance.id
            name = str(form.instance.imgrec)  # yolov5_master/number/c028_LRUKa6E.jpg    or  yolov5_master/number/well_one.mp4
            # print('name: ',name)  # name:  yolov5_master/number/c006_yA0vp6S.jpg
            img_name = name.split("/")[-1]  # c006_yA0vp6S.jpg    or    well_one.mp4
            test_img = name.split("master/")[-1]  # number/c006_yA0vp6S.jpg   or number/well_one.mp4
            pre_path = detect(test_img)  # runs\detect\exp13
            pre_img = "yolov5_master/" + pre_path + "\\" + img_name  # pre_img:  yolov5_master/runs\detect\exp9\c006_WsRVGaR.jpg
            # print('pre_img: ', pre_img)

            models.WellDanger.objects.filter(id=yid).update(imgresult=pre_img)

            img_type = name.split(".")[-1]
            # print(img_type)

            os.chdir('E:\python\django_yibiao')  # 因为yolov5可能改变了，改变工作目录

            return JsonResponse({"status": True, "url": name, "pre_url": pre_img,"img_type": img_type})


        return JsonResponse({"status": False, "error": form.errors})
    except Exception as e:
        os.chdir('E:\python\django_yibiao')  # 因为ocr可能改变了，改变工作目录
        return JsonResponse({"status": False,"msg": "检测失败，数据异常"})


'''小盖板识别列表'''
def well_list(request):
    user_id = request.session["info"]["id"]
    queryset = models.WellDanger.objects.filter(admin_id=user_id).order_by("-id")
    page_object = Pagination(request,queryset,page_size=5)
    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }
    return render(request, 'well_list.html', context)

def well_del(request):
    '''删除图片'''
    tid = request.GET.get("uid")
    Img_ocr = models.WellDanger.objects.filter(id=tid).first()
    print(Img_ocr)
    if not Img_ocr:
        return JsonResponse({"status": False, "error": "删除失败，数据不存在"})

    img_name = str(Img_ocr.imgrec)  # yolov5_master/number/39_F2KgiDa.jpg
    # print(img_name)  # rec/001_bwajbah.jpg
    # print(os.getcwd())  # E:\python\django_yibiao
    # print(img_name)    # yolov5_master/number/39_F2KgiDa.jpg
    os.chdir('E:\python\django_yibiao')  # 改变工作目录
    paths = glob.glob(os.path.join('yibiao_ocr', img_name))
    # 删除名称为img_name图像
    for file in paths:
        # print(file)   # yibiao_ocr/TemplateLib/code.png
        os.remove(file)

    img_result = str(Img_ocr.imgresult)  # yolov5_master/runs\detect\exp11\39.jpg
    paths = glob.glob(os.path.join('yibiao_ocr', img_result))

    for file in paths:
        # print(file)   # yibiao_ocr/yolov5_master/runs\detect\exp11\39.jpg
        os.remove(file)

    models.WellDanger.objects.filter(id=tid).delete()
    return JsonResponse({"status": True})