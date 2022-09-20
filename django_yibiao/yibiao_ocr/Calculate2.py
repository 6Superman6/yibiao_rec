import math

def get_rad_val(rad,c_x, c_y,a,maxd,fir_d,sec_d,scale):
    # center=[385,535]
    #计算角度
    center=[c_x, c_y]

    # 第0组实验
    # a = {0: (52, 189), 10:(85,358), 20: (90,300), 30: (85, 238),40:(100,175),50:(140,125),
    #              60: (195, 95), 70: (257,80), 80: (317,80), 90: (380,90), 100: (445,110),
    #              110: (490,160), 120: (510,225), 130: (520,290), 140: (510,355), 150: (500,425)}
    # 第1组实验——存在问题
    # a = {0: (170,710), 100:(130,530), 200: (200,340), 300: (400, 245),400:(600,330),500:(640,530),
    #              600: (580, 715)}

    # 第2组实验
    # a = {0: (200,500), 20:(140,400), 40:(190,265), 60:(270,170),80:(385,130),
    #     100:(500,170), 120: (600,250), 140:(610,385), 160: (550,505)}

    # 第3组实验
    # a = {0: (170, 470), 200: (130, 290), 400: (220, 130),
    #      600: (420, 120), 800: (550, 270), 1000: (500, 460)}
    # 第4组实验
    # a={0:(150,370),0.4:(120,205),0.8:(290,90),
    #    1.2:(455,218),1.6:(410,425)}

    # print('rad: ',rad)
    # print('c_x: ', c_x)
    # print('c_y: ', c_y)
    # print('a: ', a)
    # print('zc: ', zc)
    # print('maxd: ', maxd)
    # print('fir_d: ', fir_d)
    # print('sec_d: ', sec_d)
    # print('scale: ', scale)


    count = 0
    result = {}

    # *************确定zc值**************

    zc_list = {}
    for i in range(1, 10):
        zc_list[i] = dict()

    # *************确定zc值**************
    for k, v in a.items():
        r = math.acos((v[0] - center[0]) / ((v[0] - center[0]) ** 2 + (v[1] - center[1]) ** 2) ** 0.5)
        r = r * 180 / math.pi
        a[k] = r
        for i in range(1, 10):
            t_r = r
            if count >= i and k != maxd:  # 可修改，视每个表的情况而定，保证lst中递增排序
                # print('rr: ',r)
                t_r = 360 - t_r
            zc_list[i][k] = t_r
            # print('sdf: ',k, r)
        # *************确定zc值**************
        # if count >= 4 and k != 100:  # 可修改，视每个表的情况而定，保证lst中递增排序
        #     # print('rr: ',r)
        #     r=360-r
        #     # print('sdf: ',k, r)
        # result[k]=r
        count += 1
    # print("各刻度对应角度:", result)
    # print('zc_list: ', zc_list)
    # 第0组实验
    # d=360-result[90]+result[100]#各刻度第一次最大值到最小值
    # d1=360-result[90]

    # 第1组实验————有问题
    # d=360-result[200]+result[300]
    # d1=360-result[200]
    # t=200+100*(d1/d)

    # 第2组实验
    # d=360-result[80]+result[100]
    # d1=360-result[80]
    # t=90+10*(d1/d)

    new_lst = {}
    zero_lst = {}
    for i in range(1, 10):
        d = 360 - zc_list[i][fir_d] + zc_list[i][sec_d]
        d1 = 360 - zc_list[i][fir_d]
        t = fir_d + scale * (d1 / d)  # t=92，刻度为92就是0度的起始位置
        zero_lst[i] = t
        # print('d,d1: ', d, d1)
        # print('t=', t)
        zc_list[i][t] = 0
        result_list = zc_list[i].items()
        # print('result_list: ', result_list)
        # 匿名函数lambda：是指一类无需定义标识符（函数名）的函数或子程序。
        # lambda 函数可以接收任意多个参数 (包括可选参数) 并且返回单个表达式的值。
        # key=lambda x:x[1]
        # print(key)
        lst = sorted(result_list, key=lambda x: x[1])
        new_lst[i] = lst
    # print('new_lst: ', new_lst)

    # 第3组实验
    # d = 360 - result[fir_d] + result[sec_d]
    # d1 = 360 - result[fir_d]
    # t = fir_d + scale * (d1 / d)

    # 第4组实验
    # d=360-result[1.2]+result[1.6]
    # d1=360-result[1.2]
    # t=1.2+0.4*(d1/d)

    # result[t] = 0
    # result_list = result.items()
    # lst = sorted(result_list, key=lambda x: x[1])
    # '''排序后的刻度和坐标：'''
    # print('刻度根据角度排序后lst: ',lst)

    for i in range(1, 10):
        result = zc_list[i]
        lst = new_lst[i]
        # print('tttt: ')
        # print('type: ', type(lst))
        t = 1
        zero = zero_lst[i]
        # print('zero: ', zero)
        # print('result: ', result)
        for k, v in lst:
            # print('k,v: ',k,v)     # k,v:  92.53470094976221 0
            if k == zero:
                pre_key = k
                continue
            if k > pre_key and k > zero:
                if v > 90:
                    t = 0
            elif k > pre_key:
                if v < 90:
                    t = 0
            if k < pre_key and k < zero:
                if v < 90:
                    t = 0
            if k < pre_key and k < zero and pre_key < zero:
                t = 0
            pre_key = k
        if t == 1:
            break
    print('result: ', result)
    print('lst: ', lst)


    #计算读数
    old=None
    for k, v in lst:
        # print(k,v)
        if rad > v :
            old = k
    r=result[old]
    d=rad-r
    nx=get_next(old,lst)
    ttt = old + scale * abs(d / (nx[1] - r))#第三组
    # if(ttt>maxd):
    #     ttt=ttt-old-d
    # print("刻度:",scale)
    return ttt

def get_next(c,lst):
    l=len(lst)
    n=0
    for i in range(len(lst)):
        if lst[i][0]==c:
            n=i+1
            if n==l:
                n=0
            break
    return lst[n]