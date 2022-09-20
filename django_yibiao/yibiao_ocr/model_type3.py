# 姓名：刘超
# 开发时间：2022/2/26 20:37
import os
from glob import glob

import requests
import base64
import cv2
'''
生成模板库
'''
# print(os.getcwd())
# ocr = PaddleOCR(det_model_dir="./output/det_r50_vd/export_model",rec_model_dir="./output/rec2/mv3_none_bilstm_ctc/export_model",
#                 use_angLe_cls=True,lang='ch')

# ocr = PaddleOCR(det_model_dir="./yibiao_ocr/inference/ch_ppocr_server_v2.0_det_infer",rec_model_dir="./yibiao_ocr/inference/ch_ppocr_server_v2.0_rec_infer",
#                 cls_model_dir="./yibiao_ocr/inference/ch_ppocr_mobile_v2.0_cls_infer/",use_gpu=False,use_angLe_cls=True,use_space_char=True,lang='ch')

# if __name__ == '__main__':
#     image_files = glob('./doc/imgs/yibiao/*.*')
#     result_dir = './model_type'
#     for image_file in sorted(image_files):
#         print('\n\n')
#         print('****************')
#
#         result = ocr.ocr(image_file)
#
#         for line in result:
#             print(line)
#         print('\n\n')
#         print('****************')

def make_model_template():

    # print(os.getcwd())   # E:\python\django_yibiao
    os.chdir('E:\python\django_yibiao\yibiao_ocr')  # 改变工作目录

    image_files = glob('./TemplateLib/*.*')
    type_list = {}
    # image_files = glob('../doc/imgs/yibiao2/n001.jpg')
    # print(image_files)
    result_dir = './model_type2'
    a = 0
    fr = open('model_type2.txt', mode='w', encoding='utf8')
    for image_file in sorted(image_files):
        print('image_file: ',image_file)      # 图片完整地址   ./TemplateLib\013.jpg
        # 字符串
        # type_key = image_file.split('\\')[1]    # 图片名称
        '''重新组合图片名称和路径'''
        img_path_name = image_file.split('\\')
        type_path = img_path_name[0]
        type_key = img_path_name[1]
        new_image_file = type_path + '/' + type_key  # 去除转义字符的图片完整地址
        # print('new_image_file: ', new_image_file)
        '''重新组合图片名称和路径'''
        # print(type_key)                         # 图片名称
        type_value = ""  # 图像识别出来的文字组合字符串

        # result = ocr.ocr(image_file)

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
        f = open(new_image_file, 'rb')
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
            # result:  [{'words': '80'}, {'words': '60'}, {'words': '100'}, {'words': 'PFP SERIES'}, {'words': '40'}, {'words': '120'}, {'words': '二'}, {'words': '20'}, {'words': '140'}, {'words': '山'}, {'words': '19122643'}, {'words': '160'}, {'words': 'A0C1.6'}, {'words': 'WINIERS'}, {'words': 'psi'}, {'words': '1963'}, {'words': 'www.winters.com'}]
            result = response.json()['words_result']
            # print('result: ',result)
            for i in result:
                type_value = type_value + i['words']

        # print('type_value: ', type_value)  # 图像识别出来的文字组合字符串
        # print('image_file: ',image_file)

        # print(type_value)  # 8060100PFP SERIES40120二20140山19122643160A0C1.6WINIERSpsi1963www.winters.com
        # print(image_file)  # ./TemplateLib\002.jpg

        # *****************************************************************************************
        # f.write('{},{}\n'.format(os.path.basename(type_key), type_value))     # 读入test1.txt文件中
        # type_list[type_key] = type_value    # 将图片名称和对应字符串放入到字典中
        # *****************************************************************************************
        fr.write('{},{}\n'.format(new_image_file, type_value))  # 读入test1.txt文件中
        type_list[new_image_file] = type_value  # 将图片名称和对应字符串放入到字典中
        # *****************************************************************************************
        # print('image_file: ',image_file)
        # 显示结果
        a = a + 1

        # print('\n\n')
        # print('****************')
    fr.close()
    print(type_list)

# if __name__ == '__main__':
#     make_model_template()