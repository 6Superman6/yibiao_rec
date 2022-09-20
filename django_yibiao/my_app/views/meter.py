# 姓名：刘超
# 开发时间：2022/7/13 15:25
# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,"hello.html")