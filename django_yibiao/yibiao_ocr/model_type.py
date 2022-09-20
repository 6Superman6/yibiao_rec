# 姓名：刘超
# 开发时间：2022/2/26 20:37
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import os
from glob import glob
import cv2
'''
生成模板库
'''

# ocr = PaddleOCR(det_model_dir="./output/det_r50_vd/export_model",rec_model_dir="./output/rec2/mv3_none_bilstm_ctc/export_model",
#                 use_angLe_cls=True,lang='ch')
ocr = PaddleOCR(det_model_dir="./inference/ch_ppocr_server_v2.0_det_infer",rec_model_dir="./inference/ch_ppocr_server_v2.0_rec_infer",
                cls_model_dir="./inference/ch_ppocr_mobile_v2.0_cls_infer/",use_gpu=False,use_angLe_cls=True,use_space_char=True,lang='ch')

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

if __name__ == '__main__':
    # image_files = glob('./img_model/*.*')
    image_files = glob('./TemplateLib/*.*')
    type_list = {}
    # image_files = glob('../doc/imgs/yibiao2/n001.jpg')
    print(image_files)
    result_dir = './model_type2'
    a = 0
    f = open('model_type2.txt', mode='w', encoding='utf8')
    for image_file in sorted(image_files):
        # print('image_file: ',image_file)      # 图片完整地址   ./TemplateLib\013.jpg
        # 字符串
        # type_key = image_file.split('\\')[1]    # 图片名称
        '''重新组合图片名称和路径'''
        img_path_name = image_file.split('\\')
        type_path = img_path_name[0]
        type_key = img_path_name[1]
        new_image_file = type_path + '/' + type_key  # 去除转义字符的图片完整地址
        print('new_image_file: ',new_image_file)
        '''重新组合图片名称和路径'''
        # print(type_key)                         # 图片名称
        type_value = ""  # 图像识别出来的文字组合字符串
        # result = ocr.ocr(image_file)
        result = ocr.ocr(new_image_file)
        for line in result:
            print('line: ',line)
            iter_s = line[1][0]  # 图像中识别的实际数据
            print('iter_s: ',iter_s)
            type_value = type_value + iter_s  # 组合字符串
        print('type_value: ', type_value)  # 图像识别出来的文字组合字符串
        # print('image_file: ',image_file)

        # *****************************************************************************************
        # f.write('{},{}\n'.format(os.path.basename(type_key), type_value))     # 读入test1.txt文件中
        # type_list[type_key] = type_value    # 将图片名称和对应字符串放入到字典中
        # *****************************************************************************************
        f.write('{},{}\n'.format(new_image_file, type_value))  # 读入test1.txt文件中
        type_list[new_image_file] = type_value  # 将图片名称和对应字符串放入到字典中
        # *****************************************************************************************
        # print('image_file: ',image_file)
        # 显示结果
        image = Image.open(new_image_file).convert('RGB')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        im_show = draw_ocr(image, boxes, txts, scores, font_path='./doc/simfang.ttf')
        im_show = Image.fromarray(im_show)
        res = result_dir + '/' + type_key
        # print(res)   # 生成识别图片地址
        # im_show.save('./model_type/result1.jpg')  # 结果图片保存
        im_show.save(res)  # 结果图片保存
        a = a + 1

        print('\n\n')
        print('****************')
    f.close()
    print(type_list)