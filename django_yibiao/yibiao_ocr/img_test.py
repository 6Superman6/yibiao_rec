# 姓名：刘超
# 开发时间：2022/4/5 10:07
import cv2
img_s = cv2.imread('./TemplateLib/temp013-2.jpg')
print(img_s)
'''转换颜色空间,转换为灰度图像'''
img = cv2.cvtColor(img_s, cv2.COLOR_BGR2GRAY)
#
cv2.imshow('灰度：', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
