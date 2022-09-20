# 姓名：刘超
# 开发时间：2022/7/19 15:05
# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse,redirect
from my_app.utils.pagination import Pagination
from my_app import models
from my_app.utils.bootstrap import BootStrapModelForm
from django import forms
from django.http import JsonResponse
from yibiao_ocr.img_ocr_rec import ocr_rec
import os
import glob

# 免除post请求的csrf认证
from django.views.decorators.csrf import csrf_exempt

'''图片上传的ModelForm'''
class OcrImgModelForm(BootStrapModelForm):

    bootstrap_exclude_fields = ["img"]  # 排除不想添加样式的字段

    class Meta:
        model = models.ImgOcrRec
        exclude = ["img_result", "admin"]  # 排除img_result和admin后的所有属性（排除订单号和所属用户）
        widgets = {
            "img": forms.FileInput(attrs={"accept": "image/*"}),
            # 限制input file上传类型只能是图片: <input type="file" accept="image/*">
        }

'''ocr文字识别列表'''
def ocr(request):
    form = OcrImgModelForm()
    return render(request,'ocr.html',{"form": form})

'''识别'''
@csrf_exempt
def rec(request):
    form = OcrImgModelForm(data=request.POST, files=request.FILES)

    try:
        if form.is_valid():
            # 固定设置管理员ID，去哪里获取？(当前登录用户的id)
            form.instance.admin_id = request.session["info"]["id"]
            form.save()
            yid = form.instance.id
            name = str(form.instance.img)  # rec/1.jpg
            result = ocr_rec(name)
            print(result)
            models.ImgOcrRec.objects.filter(id=yid).update(img_result=result)

            os.chdir('E:\python\django_yibiao')  # 因为ocr可能改变了，改变工作目录
            return JsonResponse({"status": True, "msg": result, "url": name})

        return JsonResponse({"status": False, "error": form.errors})
    except Exception as e:
        os.chdir('E:\python\django_yibiao')  # 因为ocr可能改变了，改变工作目录
        return JsonResponse({"status": False,"msg": "生成失败，数据异常"})


'''ocr文字识别列表'''
def ocr_list(request):
    user_id = request.session["info"]["id"]
    queryset = models.ImgOcrRec.objects.filter(admin_id=user_id).order_by("-id")
    page_object = Pagination(request,queryset,page_size=5)
    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }
    return render(request, 'ocr_list.html', context)

def ocr_del(request):
    '''删除图片'''
    tid = request.GET.get("uid")
    Img_ocr = models.ImgOcrRec.objects.filter(id=tid).first()
    if not Img_ocr:
        return JsonResponse({"status": False, "error": "删除失败，数据不存在"})

    img_name = str(Img_ocr.img)  # rec/1.png
    # print(img_name)  # rec/001_bwajbah.jpg
    # print(os.getcwd())  # E:\python\django_yibiao
    os.chdir('E:\python\django_yibiao')  # 改变工作目录
    paths = glob.glob(os.path.join('yibiao_ocr', img_name))
    # 删除名称为img_name图像
    for file in paths:
        # print(file)   # yibiao_ocr/TemplateLib/code.png
        os.remove(file)

    models.ImgOcrRec.objects.filter(id=tid).delete()
    return JsonResponse({"status": True})