import math

def get_rad_val(rad,c_x, c_y,a,zc,maxd,fir_d,sec_d,scale):
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
    for k, v in a.items():
        r = math.acos((v[0] - center[0]) / ((v[0] - center[0]) ** 2 + (v[1] - center[1]) ** 2) ** 0.5)
        r = r * 180 / math.pi
        a[k] = r
        if count >= zc and k != maxd:  # 第三组
            # if count >= 2 and k != 1.6:#第四组
            r = 360 - r
            # print(k, r)
        result[k] = r
        count += 1
    # print("各刻度对应角度:", result)

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

    # 第3组实验
    d = 360 - result[fir_d] + result[sec_d]
    d1 = 360 - result[fir_d]
    t = fir_d + scale * (d1 / d)

    # 第4组实验
    # d=360-result[1.2]+result[1.6]
    # d1=360-result[1.2]
    # t=1.2+0.4*(d1/d)

    result[t] = 0
    result_list = result.items()
    lst = sorted(result_list, key=lambda x: x[1])
    '''排序后的刻度和坐标：'''
    print("各刻度对应角度:", result)
    print('刻度根据角度排序后lst: ',lst)
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