import cv2
import numpy as np
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from math import cos, pi, sin
# from Calculate import get_rad_val
from yibiao_ocr.Calculate2 import get_rad_val
import warnings

from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import os
from glob import glob
import cv2
import os

from fuzzywuzzy import fuzz

'''
检测仪表类型
'''

ocr = PaddleOCR(det_model_dir="./yibiao_ocr/inference/ch_ppocr_server_v2.0_det_infer",rec_model_dir="./yibiao_ocr/inference/ch_ppocr_server_v2.0_rec_infer",
                cls_model_dir="./yibiao_ocr/inference/ch_ppocr_mobile_v2.0_cls_infer/",use_gpu=False,use_angLe_cls=True,use_space_char=True,lang='ch')

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
               'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
method = cv2.TM_CCOEFF

def get_match_rect(template,img,method):
    '''获取模板匹配的矩形的左上角和右下角的坐标'''
    w, h = template.shape[1],template.shape[0]
    res = cv2.matchTemplate(img, template, method)
    mn_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # 使用不同的方法，对结果的解释不同
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    return top_left,bottom_right

def get_center_point(top_left,bottom_right):
    '''传入左上角和右下角坐标，获取中心点'''
    c_x, c_y = ((np.array(top_left) + np.array(bottom_right)) / 2).astype(np.int64)
    return c_x,c_y

def get_circle_field_color(img,center,r,thickness):
    '''获取中心圆形区域的色值集'''
    temp=img.copy().astype(np.int64)
    cv2.circle(temp,center,r,-100,thickness=thickness)
    return img[temp == -100]

def v2_by_center_circle(img,colors):
    '''二值化通过中心圆的颜色集合'''
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            a = img[i, j]
            if a in colors:
                img[i, j] = 0
            else:
                img[i, j] = 255

def v2_by_k_means(img):
    '''使用k-means二值化'''
    original_img = np.array(img, dtype=np.float64)
    src = original_img.copy()
    delta_y = int(original_img.shape[0] * (0.4))
    delta_x = int(original_img.shape[1] * (0.4))
    original_img = original_img[delta_y:-delta_y, delta_x:-delta_x]
    h, w, d = src.shape
    dts = min([w, h])
    r2 = (dts / 2) ** 2
    c_x, c_y = w / 2, h / 2
    a: np.ndarray = original_img[:, :, 0:3].astype(np.uint8)
    # 获取尺寸(宽度、长度、深度)
    height, width = original_img.shape[0], original_img.shape[1]
    depth = 3
    image_flattened = np.reshape(original_img, (width * height, depth))
    '''
    用K-Means算法在随机中选择1000个颜色样本中建立64个类。
    每个类都可能是压缩调色板中的一种颜色。
    '''
    image_array_sample = shuffle(image_flattened, random_state=0)
    estimator = KMeans(n_clusters=2, random_state=0)
    estimator.fit(image_array_sample)
    '''
    我们为原始图片的每个像素进行类的分配。
    '''
    src_shape = src.shape
    new_img_flattened = np.reshape(src, (src_shape[0] * src_shape[1], depth))
    cluster_assignments = estimator.predict(new_img_flattened)
    '''
    我们建立通过压缩调色板和类分配结果创建压缩后的图片
    '''
    compressed_palette = estimator.cluster_centers_
    # print(compressed_palette)
    a = np.apply_along_axis(func1d=lambda x: np.uint8(compressed_palette[x]), arr=cluster_assignments, axis=0)
    img = a.reshape(src_shape[0], src_shape[1], depth)
    # print(compressed_palette[0, 0])
    threshold = (compressed_palette[0, 0] + compressed_palette[1, 0]) / 2
    img[img[:, :, 0] > threshold] = 255
    img[img[:, :, 0] < threshold] = 0
    # cv2.imshow('sd0', img)
    for x in range(w):
        for y in range(h):
            distance = ((x - c_x) ** 2 + (y - c_y) ** 2)
            if distance > r2:
                pass
                img[y, x] = (255, 255, 255)
    # cv2.imshow('sd', img)
    # cv2.waitKey(10)
    # if cv2.waitKey(100)==27:
    #     print("sd关闭")

    cv2.destroyAllWindows()
    return img

def get_pointer_rad(img,c_x,c_y):
    '''获取角度'''
    shape = img.shape

    # *******kai******
    # 中心
    c_y, c_x, depth = int(shape[0] / 2), int(shape[1] / 2), shape[2]
    print('c_y, c_x: ',c_y, c_x)
    # *******kai******

    x1=c_x+c_x*0.8
    src = img.copy()

    freq_list = []

    for i in range(361):
        x = (x1 - c_x) * cos(i * pi / 180) + c_x
        y = (x1 - c_x) * sin(i * pi / 180) + c_y

        temp = src.copy()

        cv2.line(temp, (c_x, c_y), (int(x), int(y)), (0, 0, 255), thickness=3)#在temp中画一条（c_x,c_y）到点（x，y）的红色的直线

        t1 = img.copy()
        t1[temp[:, :, 2] == 255] = 255#如果某个刻度值对应点的红色通道灰度值为255，则将t1中同样位置的该点的颜色置为255（白色）
        c = img[temp[:, :, 2] == 255]#将temp中红色通道为白色（255）的位置置为True，其他为false
        points = c[c == 0]#将C中等于0的点位置坐标传给points
        freq_list.append((len(points), i))#freq_list 保存points的长度和此时的角度i
        # cv2.line(temp, (c_x,c_y),(155,565), (255, 0, 0), thickness=3)  # 刻度值蓝色的直线
        # print("freq_list：",freq_list)
        # cv2.imshow('red line', temp)
        # cv2.imshow('line cover', t1)

        # 绘制坐标点！！！！！！！！！！！！！！！
        # point_list=[
        #             (220,265),
        #             (110,367), (100,300),(105,230),(125,160),(195,130),
        #             (270,130),(325,180),(360,250),(340,320),(320,350)]
        #
        #
        # for point in point_list:
        #     cv2.circle(t1, point, 3, (0, 0, 255),thickness=3)

        # cv2.imshow('img', t1)

        # cv2.waitKey(1)
        #cv2.waitKey(0)

    print('当前角度：', max(freq_list, key=lambda x: x[0]), '度')  # 取长度最大，即指针覆盖面积最大的点（位置）

    cv2.destroyAllWindows()

    return max(freq_list, key=lambda x: x[0])

'''无用方法，不能使用模板匹配得到的中心坐标'''
def get_pointer_rad_2(img,c_x,c_y):
    '''获取角度'''
    shape = img.shape

    # *******kai******
    # 中心
    c_y0, c_x0, depth = int(shape[0] / 2), int(shape[1] / 2), shape[2]
    print('c_y, c_x: ',c_y, c_x)
    # *******kai******

    x1=c_x+c_x*0.8
    src = img.copy()

    freq_list = []

    for i in range(361):
        x = (x1 - c_x) * cos(i * pi / 180) + c_x
        y = (x1 - c_x) * sin(i * pi / 180) + c_y

        temp = src.copy()

        cv2.line(temp, (c_x, c_y), (int(x), int(y)), (0, 0, 255), thickness=3)#在temp中画一条（c_x,c_y）到点（x，y）的红色的直线

        t1 = img.copy()
        t1[temp[:, :, 2] == 255] = 255#如果某个刻度值对应点的红色通道灰度值为255，则将t1中同样位置的该点的颜色置为255（白色）
        c = img[temp[:, :, 2] == 255]#将temp中红色通道为白色（255）的位置置为True，其他为false
        points = c[c == 0]#将C中等于0的点位置坐标传给points
        freq_list.append((len(points), i))#freq_list 保存points的长度和此时的角度i
        # cv2.line(temp, (c_x,c_y),(155,565), (255, 0, 0), thickness=3)  # 刻度值蓝色的直线
        # print("freq_list：",freq_list)
        # cv2.imshow('red line', temp)
        # cv2.imshow('line cover', t1)

        # 绘制坐标点！！！！！！！！！！！！！！！
        # point_list=[
        #             (220,265),
        #             (110,367), (100,300),(105,230),(125,160),(195,130),
        #             (270,130),(325,180),(360,250),(340,320),(320,350)]
        #
        #
        # for point in point_list:
        #     cv2.circle(t1, point, 3, (0, 0, 255),thickness=3)

        # cv2.imshow('img', t1)

        # cv2.waitKey(1)
        #cv2.waitKey(0)

    print('当前角度：', max(freq_list, key=lambda x: x[0]), '度')  # 取长度最大，即指针覆盖面积最大的点（位置）

    cv2.destroyAllWindows()

    return max(freq_list, key=lambda x: x[0])


'''找到测试图片对应的模板图片'''
def get_type(type_value,type_list):
    score = -1
    img_type = ""  # 测试图片对应的模板图片
    for key in type_list:   # key为图片名称
        img_value = type_list[key]   # img_value为图片所对应的字符串
        rate = fuzz.ratio(type_value, img_value)   # 计算两个字符串的相似度
        if score < rate:
            img_type = key
            score = rate
    return img_type

def getTemplate(img_name):
    print(os.getcwd())
    # img_name = "img_test_2/1.jpg"

    '''读取模板字符串文件，用于匹配相似度'''
    type_list = {}  # 将图片名称和对应字符串放入到字典中（模板）
    fp = open('./model_type2.txt', mode='r', encoding='utf8')        # model_type.txt是模板库文件
    lines = fp.readlines()
    for sline in lines:
        if sline != '\n':
            str_list = sline.split(',')
            # print(str_list)    # 文档中的行数据
            type_key = str_list[0]
            type_value = str_list[1].rstrip('\n')  # 删除字符串末尾的指定字符rstrip()方法，删除末尾的\n
            # print('type_key: type_value',type_key,type_value)
            type_list[type_key] = type_value
    fp.close()
    # print(type_list)

    '''读取模板字符串文件，用于匹配相似度'''
    model_list = {}  # 测试图片:模板图片
    # image_files = glob('./img_test/*.*')
    '''原'''
    # image_files = glob('./img_test/*.*')
    '''原'''
    image_files = glob('./'+img_name)
    # image_files = glob('../doc/imgs/yibiao2/n001.jpg')
    # print(image_files)
    result_dir = './img_type'
    a = 0
    f = open('make_type.txt', mode='w', encoding='utf8')
    f_result = open('img_type_result.txt', mode='w', encoding='utf8')
    for image_file in sorted(image_files):
        # print('image_file: ',image_file)      # 图片完整地址   ./img_test\013.jpg
        # 字符串
        # type_key = image_file.split('\\')[1]  # 图片名称

        # print("image_file: ",image_file)       # image_file:  ./img_test_2/(1).jpg
        new_image_file = image_file
        print('new_image_file: ', new_image_file)
        '''重新组合图片名称和路径'''
        type_key = image_file.split('/')[-1]  # 图片名称
        print(type_key)
        type_value = ""  # 图像识别出来的文字组合字符串
        result = ocr.ocr(new_image_file)
        for line in result:
            # print('line: ',line)
            iter_s = line[1][0]  # 图像中识别的实际数据
            # print('iter_s: ',iter_s)
            type_value = type_value + iter_s  # 组合字符串
        print('图像识别出来的文字组合字符串type_value: ', type_value)  # 图像识别出来的文字组合字符串
        '''os.path.basename(type_key)只会保留图片名称'''
        f.write('{},{}\n'.format(os.path.basename(new_image_file), type_value))  # 读入test1.txt文件中

        # *****************************
        '''找到测试图片对应的模板图片'''
        img_Type = get_type(type_value, type_list)
        model_list[new_image_file] = img_Type  # 将图片名称和对应模板图片放入到字典中
        # f_result.write('{}:{}\n'.format(os.path.basename(type_key), img_Type))  # 读入test1.txt文件中
        f_result.write('{}:{}\n'.format(new_image_file, img_Type))  # 读入test1.txt文件中
        # *****************************

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
    f_result.close()
    print('测试图片：对应模板 ', model_list)
    # return(type_key) # 返回图像名称如n01.jpg
    name = type_key.split('.')[0]     # 图片名称 如n01.jpg的n01
    return model_list  # 返回测试图像：对应模板的字典

def img_rec(img_name):

    # print(os.getcwd())   # E:\python\django_yibiao
    os.chdir('E:\python\django_yibiao\yibiao_ocr')  # 改变工作目录


    # 读取所有的测试图片,获取测试图片对应的模板
    img_and_model_list = getTemplate(img_name)
    return img_and_model_list


def img_rec_result(img_and_model_list,Template):
    # print(os.getcwd())   # E:\python\django_yibiao
    os.chdir('E:\python\django_yibiao\yibiao_ocr')  # 改变工作目录


    # img_and_model_list字典：测试图片路径地址：模板图片路径地址
    print('img_and_model_list: ', img_and_model_list)
    img_result = 0.0
    for key_name in img_and_model_list:
        template_str = key_name
        # print('template_str: ',template_str)    # ./img_test/(3).jpg

        img_s = cv2.imread(template_str)  # 读取测试图片
        template_img = img_and_model_list[template_str]
        print('测试图像：模板图像：', template_str, template_img)
        template1 = cv2.imread(template_img)  # 读取测试图片对应的模板图片
        template2 = cv2.imread(template_img)  # 读取测试图片对应的模板图片


        c_x = float(Template.c_x)
        c_y = float(Template.c_y)
        a = eval(Template.a)  # #刻度坐标点
        # zc = int(data_item['zc'])  # 好像是说几个刻度点
        # maxd = data_item['maxd']
        maxd = float(Template.maxd)  # 最大刻度
        # fir_d = data_item['fir_d']
        fir_d = float(Template.fir_d)  # 骤然变化最小点
        # sec_d = data_item['sec_d']
        sec_d = float(Template.sec_d)  # 骤然变化最大点
        # scale = data_item['scale']
        scale = float(Template.scale)  # 一格刻度
        # {'c_x': '118', 'c_y': '115', 'a': '{0:(45,162),0.1:(34,107),0.2:( 63,48 ),0.3:(126,28),0.4:(186,59),0.5:(206,123),0.6:(175,182)}', 'zc': '2', 'maxd': '0.6', 'fir_d': '0.5', 'sec_d': '0.6', 'scale': '0.1'}
        # print(data_item)

        img = cv2.cvtColor(img_s, cv2.COLOR_BGR2GRAY)
        template1 = cv2.cvtColor(template1, cv2.COLOR_BGR2GRAY)
        # 匹配并返回矩形坐标
        top_left, bottom_right = get_match_rect(template1, img, method)
        c_x0, c_y0 = get_center_point(top_left, bottom_right)
        # print("匹配后的中心点坐标：", c_x0, c_y0)

        # 绘制矩形
        cv2.rectangle(img_s, top_left, bottom_right, 255, 2)
        # cv2.imshow('img', cv2.resize(img_s, (int(img.shape[1] * 0.5), int(img.shape[0] * 0.5))))
        # cv2.waitKey(10)
        cv2.destroyAllWindows()

        #################################################################
        new = img_s[top_left[1]:bottom_right[1] + 1, top_left[0]:bottom_right[0] + 1]  # 这句话没弄懂在干嘛
        # template2 = cv2.imread('temp3-2.jpg')
        top_left, bottom_right = get_match_rect(template2, new, method=method)
        new_ = new[top_left[1]:bottom_right[1] + 1, top_left[0]:bottom_right[0] + 1]
        # 二值化图像
        # cv2.imshow('二值化图像', new_)
        img = v2_by_k_means(new_)
        rad = get_pointer_rad(img, c_x0, c_y0)
        # rad = get_pointer_rad_2(img, c_x0, c_y0)

        # cv2.waitKey(0)
        #################################################################

        # print('对应刻度', get_rad_val(rad[1], c_x, c_y, a, zc, maxd, fir_d, sec_d, scale))
        img_result = get_rad_val(rad[1], c_x, c_y, a, maxd, fir_d, sec_d, scale)
        print('对应刻度', img_result)  # 对应刻度 0.11503240573944025
        print('\n**************************************************')

    return img_result

# if __name__ == '__main__':
#     img_result = img_rec('img_test_2/1.jpg')
#     print('img_result: ',img_result)     # img_result:  0.11503240573944025
