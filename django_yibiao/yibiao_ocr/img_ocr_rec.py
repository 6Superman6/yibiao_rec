# 姓名：刘超
# 开发时间：2022/7/19 17:51
# -*- coding: utf-8 -*-
from PIL import ImageGrab
from tkinter import *

import requests
import base64
import os
from PIL import ImageGrab

from tkinter import *

def ocr_rec(img_name):

    result = ""

    # print(os.getcwd())   # E:\python\django_yibiao
    os.chdir('E:\python\django_yibiao\yibiao_ocr')  # 改变工作目录

    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=wgEHks0l6MCpalbs3lPuFX1U&client_secret=Z4Rn4ghBx9k06fUYPmSEIRbCFvWFxLyQ'
    response = requests.get(host)
    # if response:
    #     print(response.json()['access_token'])

    '''
    通用文字识别（高精度版）
    '''
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件
    f = open('./'+img_name, 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img}
    # 获取后的Token的调用
    # access_token = '24.024b834067301333c823615ac27eaeba.2592000.1660788317.282335-24065278'
    access_token = response.json()['access_token']
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        # print(response.json())
        img_rec = response.json()
        for i in response.json()['words_result']:
            result = result + i['words'] + "\n"
            # print(i['words'])
    return result


# print(rec('rec/1.jpg'))
'''
03
0.2
压力表
0.4
MPa
0.1
0.5
0
Me
02270150
06
'''