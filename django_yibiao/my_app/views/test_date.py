# 姓名：刘超
# 开发时间：2022/7/15 11:33
# -*- coding: utf-8 -*-
import datetime
now_time = datetime.datetime.now()
print(now_time)

img_name = "./TemplateLib/template.jpg"
msg = img_name.split("./")   # ['', 'TemplateLib/template.jpg']
print(msg)