# 姓名：刘超
# 开发时间：2022/6/21 15:56
# -*- coding: utf-8 -*-
from django import forms

class BootStrap:
    bootstrap_exclude_fields = []   # 排除那些不想添加样式的属性

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 循环ModelForm中的所有字段，给每个字段的插件设置
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:  # 排除那些不想添加样式的属性
                continue
            # 字段中有属性，保留原来的属性，没有属性，才增加。
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }

class BootStrapModelForm(BootStrap,forms.ModelForm):
    pass

class BootStrapForm(BootStrap,forms.Form):
    pass