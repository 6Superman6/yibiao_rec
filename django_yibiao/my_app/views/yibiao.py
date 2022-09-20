# 姓名：刘超
# 开发时间：2022/7/13 17:45
# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse,redirect
from my_app.utils.pagination import Pagination
from my_app import models
from my_app.utils.bootstrap import BootStrapModelForm
from django import forms
from django.http import JsonResponse
from yibiao_ocr.template_matching4 import img_rec,img_rec_result

import os
import glob

'''仪表信息表'''
def yibiao_list(request):
    user_id = request.session["info"]["id"]
    queryset = models.Yibiao.objects.filter(admin_id=user_id).order_by("-id")
    page_object = Pagination(request,queryset,page_size=5)
    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }
    return render(request, 'yibiao_list.html', context)

class YibiaoModelForm(BootStrapModelForm):

    bootstrap_exclude_fields = ["img"]  # 排除不想添加样式的字段

    class Meta:
        model = models.Yibiao
        exclude = ["img_result", "admin","img_name"]  # 排除oid和admin后的所有属性（排除订单号和所属用户）
        widgets = {
            "img": forms.FileInput(attrs={"accept": "image/*"}),
            # 限制input file上传类型只能是图片: <input type="file" accept="image/*">
        }

'''上传仪表图片'''
def yibiao_add(request):
    title = "上传仪表图像"
    req_method =request.method
    if req_method == 'GET':
        form = YibiaoModelForm()
        return render(request,'upload_form.html',{"title": title,"form": form})
    form = YibiaoModelForm(data=request.POST,files=request.FILES)

    if form.is_valid():
        # 对于文件：自动保存；
        # 字段 + 上传路径写入到数据库
        # 不用担心重复上传同名文件会被覆盖的情况，它会自动给崇明的文件加uuid

        # 固定设置管理员ID，去哪里获取？(当前登录用户的id)
        form.instance.admin_id = request.session["info"]["id"]


        form.save()
        yid = form.instance.id
        name = str(form.instance.img).split('/')[-1]
        models.Yibiao.objects.filter(id=yid).update(img_name=name)

        # return redirect('/yibiao/list/')
        return redirect('/')
    return render(request, 'upload_form.html', {"form": form, "title": title})

'''删除仪表图像'''
def yibiao_del(request,yid):
    '''在删除数据库数据的同时把对应的图片删除'''
    yibiao = models.Yibiao.objects.filter(id=yid).first()
    if not yibiao:
        return render(request,'error.html',{"msg": "数据不存在"})

    img_name = str(yibiao.img)  # img_test_2/013_agGrgE8.jpg
    print('img_name: ',img_name)  # img_test_2/001_bwajbah.jpg
    # print(os.getcwd())  # E:\python\django_yibiao
    os.chdir('E:\python\django_yibiao')  # 改变工作目录
    p_path = str(os.getcwd())
    print('p_path: ',p_path)  # p_path:  E:\python\django_yibiao
    paths = glob.glob(os.path.join('yibiao_ocr', img_name))
    # 删除名称为img_name图像
    for file in paths:
        print(file)   # yibiao_ocr\img_test_2/1.jpg
        os.remove(file)

    models.Yibiao.objects.filter(id=yid).delete()
    # return redirect('/yibiao/list/')
    return redirect('/')

'''仪表检测'''
def yibiao_detect(request,yid):
    yibiao = models.Yibiao.objects.filter(id=yid).first()
    # print(yibiao)
    if not yibiao:
        return render(request, 'error.html', {"msg": "数据不存在"})
    # print(str(yibiao.img))

    try:
        # result = img_rec(str(yibiao.img))  # img_test_2/001_kF3RmqA.jpg
        img_template = img_rec(str(yibiao.img))  # {'./img_test_2/1.jpg': './TemplateLib/template.jpg'}
        name = "./" + str(yibiao.img)   # 测试图片名称
        # 对应模板图片名称
        template_name = img_template[name].split("./")[-1]  # ['', 'TemplateLib/template.jpg']

        Template = models.Imgtemplate.objects.filter(img_template=template_name).first()

        result = img_rec_result(img_template, Template)

        # print('result: ',result)

        models.Yibiao.objects.filter(id=yid).update(img_result=result)

        # msg = {
        #     "id": yibiao.id,
        #     "img": yibiao.img,
        #     "user": yibiao.admin.username,
        #     "result": result
        # }
        # print(msg)
        # return render(request, 'error.html', {"msg": msg})
        os.chdir('E:\python\django_yibiao')  # 因为ocr可能改变了，改变工作目录
        return JsonResponse({"status": True})
    except Exception as e:
        os.chdir('E:\python\django_yibiao')  # 因为ocr可能改变了，改变工作目录
        return JsonResponse({"status": False,"msg": "检测失败，数据异常"})




