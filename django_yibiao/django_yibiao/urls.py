"""django_yibiao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app.views import meter,admin,yibiao,account,model_template,ocr,well
from django.urls import path,re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [

    # 配置media
    re_path(r'^yibiao_ocr/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='yibiao_ocr'),

    path('meter/', meter.index),

    # 登录
    path('login/', account.login),
    path('logout/', account.logout),  # 注销
    path('image/code/', account.image_code),  # 生成图像验证码

    # 用户
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('user/add/', admin.user_add),   # 用户注册
    path('admin/<int:aid>/edit/', admin.admin_edit),
    path('user/<int:aid>/edit/', admin.user_edit), # 用户更新
    path('admin/del/', admin.admin_del),
    path('admin/<int:aid>/reset/', admin.admin_reset),
    path('user/<int:aid>/reset/', admin.user_reset), # 用户更新密码

    # 仪表图像处理
    path('', yibiao.yibiao_list),  # 仪表列表（设置为成为默认的启动地址）
    # path('yibiao/list/', yibiao.yibiao_list),
    path('yibiao/add/',yibiao.yibiao_add),                # 上传仪表图像
    path('yibiao/<int:yid>/del/',yibiao.yibiao_del),      # 删除仪表图像
    path('yibiao/<int:yid>/detect/',yibiao.yibiao_detect),# 仪表检测

    # 仪表模板图像处理
    path('model/list/',model_template.model_list),        # 仪表模板列表
    path('model/add/',model_template.model_add),
    path('model/edit/',model_template.model_edit),
    path('model/del/',model_template.model_del),
    path('model/detail/',model_template.model_detail),
    path('model/make_template_msg/',model_template.make_template_msg),

    # 文字识别
    path('ocr/',ocr.ocr),
    path('ocr/rec/',ocr.rec),
    path('ocr/list/',ocr.ocr_list),
    path('ocr/del/',ocr.ocr_del),

    # 小盖板识别
    path('well/',well.well),
    path('well/rec/',well.well_rec),
    path('well/list/',well.well_list),
    path('well/del/',well.well_del),



]
