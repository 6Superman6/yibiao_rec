# 姓名：刘超
# 开发时间：2022/7/14 15:30
# -*- coding: utf-8 -*-
import os
import glob

'''
运行项目：django_yibiao项目
django_yibiao
    -yibiao_ocr/img_test_2/013_PbopCbC.jpg
    -img_delete_test.py
'''

img_name = 'img_test_2/11.jpg' # img_test_2/013_agGrgE8.jpg

paths = glob.glob(os.path.join('yibiao_ocr', img_name))
# 删除013_PbopCbC.jpg图像
for file in paths:
    print(file)
    os.remove(file)