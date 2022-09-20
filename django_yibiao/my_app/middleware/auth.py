# 姓名：刘超
# 开发时间：2022/6/29 9:19
# -*- coding: utf-8 -*-
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect

'''中间件：登录拦截器'''
class AuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        # 排除那些不需要登录就能访问的页面   (完整的url地址为：https:localhost:8080/login/)
        # request.path_info 获取当前用户请求的URL: /login/
        if request.path_info in ["/login/","/user/add/","/image/code/"]:  # 获取当前用户请求的URL /login/
            return

        # 1.读取当前访问的用户的session信息，如果能读到，说明已登陆过，就可以继续向后走。
        info_dict = request.session.get("info")  # 用户的session信息
        # print(info_dict)  # {'id': 8, 'name': 'root'}
        if info_dict:
            return

        # 2.到这说明没有登录过，重定向到登录页面
        return redirect("/login/")