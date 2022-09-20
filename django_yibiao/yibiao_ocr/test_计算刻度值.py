import math


center=[228 , 244]    # 表中心位置
# a为坐标值和对应的坐标位置
a={0:(90,380),10000:(45,270),20000:(85,140),30000:(220, 80),40000:(355,130),50000:(400,270),60000:(340,390)}
count=0
result={}    # result中存储的是列表lst中根据元组中第一个值按增序后的数据
for k ,v in a.items():
    #  带删
    # print('*****************')
    # print('v[0]: ',v[0],end='\t')
    # print('v[1]: ',v[1])
    # print('*****************')
    #  带删

    '''角度计算公式.png'''
    # 返回arccos数字
    r=math.acos((v[0]-center[0])/((v[0]-center[0])**2 + (v[1]-center[1])**2)**0.5)
    #  带删
    # print('r',r)
    #  带删
    r=r*180/math.pi     # r不出意外计算出来的是角度
    #  带删
    # print('r+', r)
    #  带删
    a[k]=r    # 把计算出来的结果r赋值给键值key
    # if count >= 4 and k != 100:
    if count >= 2 and k != 60000:       # 可修改，视每个表的情况而定，保证lst中递增排序
        r=360-r
        # print(k, r)
    result[k]=r
    count+=1
print('result: ',result)
d=360-result[50000]+result[60000]
d1=360-result[50000]
t=50000+10000*(d1/d)
# ****************
# t=0.08+0.1*(d1/d)
# t=0.52+0.1*(d1/d)
# ****************

print('d: ',d,' d1: ',d1)
# print('result[500]: ',result[500])
# print('result[600]: ',result[600])
# t=90+10*(d1/d)
print('t=',t)
result[t]=0
result_list=result.items()
# 匿名函数lambda：是指一类无需定义标识符（函数名）的函数或子程序。
# lambda 函数可以接收任意多个参数 (包括可选参数) 并且返回单个表达式的值。
# key=lambda x:x[1]
# print(key)
lst=sorted(result_list,key=lambda x:x[1])

'''
根据列表中元组的一个值寻找列表中的该值的下一个元组
'''
def get_next(c):
    l=len(lst)
    n=0
    for i in range(len(lst)):
        if lst[i][0]==c:     #遍历列表中的元组，找到元组中和c相等的值
            n=i+1            # n代表下一个元组位置
            if n==l:
                n=0
            break
    return lst[n]           # 返回列表中的下一个元组

# rad = 41
def get_rad_val(rad):
    old=None
    for k, v in lst:       # k,v分别代表元组中的两个值
        # print('k , v: ',k,v)
        if rad > v :
            old = k     # 相当于把t赋值给了old
    print('get_rad_val: ',old)                          # 92.53470094976221
    r=result[old]                       # 0
    print('r= ',r)
    d=rad-r                             # 40
    print('d= ',d)
    nx=get_next(old)                    # 根据列表中元组的一个值寻找列表中的该值的下一个元组
    print('nx= ',nx)
    # print(nx)                         # (100, 44.19307054489763)
    # print('(nx[1] - r))',d,(nx[1] - r),d/(nx[1] - r)), nx[1] = 44.19307054489763
    # print(10*abs(d/(nx[1] - r)))        # 9.051192756421461
    print('get_rad_val: ',nx)
    # t=old+10*abs(d/(nx[1] - r))         # 92.53470094976221+9.051192756421461=101.58589370618367
    t = old + 10000 * abs(d / (nx[1] - r))
    print('get_rad_val: ',t)
    return t

# print(get_next(40))
# #  带删
print('lst:',lst)
# # lst: [(92.53470094976221, 0), (100, 44.19307054489763), (20, 133.38646106711883), (30, 149.1331905488629), (40, 163.8986976008416), (50, 172.51911382047632), (60, 214.6583547055211), (70, 251.18811069748085), (80, 297.89727103094765), (90, 344.99507961713977)]
# print(result)
# # {20: 133.38646106711883, 30: 149.1331905488629, 40: 163.8986976008416, 50: 172.51911382047632, 60: 214.6583547055211, 70: 251.18811069748085, 80: 297.89727103094765, 90: 344.99507961713977, 100: 44.19307054489763, 92.53470094976221: 0}
# print(get_rad_val(0.3))
# #  带删


