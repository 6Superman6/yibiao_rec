# 姓名：刘超
# 开发时间：2022/1/21 9:25

import os

path = "runs/detect/exp24/labels" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
txts = []
for file in files: #遍历文件夹
    position = path+'//'+ file #构造绝对路径，"\\"，其中一个'\'为转义符
    # print (position)   # 输出每个txt文件的绝对路径
    names = file.split('.')
    name = '图片'+names[0]+': '
    print(name,end=' ')
    listData = dict()
    # print(type(listData))  # <class 'dict'>
    with open(position, "r",encoding='utf-8') as f:    #打开文件
        # data = f.read()
        # print(type(data))  # <class 'str'>

        data = f.readlines()   #读取文件
        # txts.append(data)

        # print(type(data))   #  <class 'dict'>
        for s in data:
            # print(s1)
            s1 = s.replace('\n','')
            str = s1.split(' ')
            key = int(str[0])
            value = float(str[1])
            # print(value)
            # print(type(str),str)
            # print(key,value)
            listData[value] = key
        # print(listData)
        # 对字典按值(value)进行排序
        # list_2 = sorted(listData.items(), key=lambda x: x[1])
        # 对字典按键(key)进行排序
        list_2 = sorted(listData.items(), key=lambda x: x[0])
        # list_3 = dict(list_2)
        # print(list_2) #  <class 'list'>
        # print(list_3)  # <class 'dict'>
        # print(list_3)
        # data_value= ""
        # result = list(list_3.keys())
        # print(result)
        # for res in result:
        #     if res == 10:
        #         print('.',end='')
        #     else:
        #         print(res,end='')
        #
        # print('\n')
        s_data = ""
        for res in list_2:
            t = res[1]
            if t==10:
                print('.',end='')
            else:
                print(t,end='')
        print('\n')


# txts = ','.join(txts)#转化为非数组类型
# print (txts)






