#图像轮廓和直方图
#图像轮廓
from PIL import Image  
from numpy import *
import matplotlib.pyplot as plt 
im = array(Image.open('d:\\test.jpg').convert('L'))  # 读取图像到数组中，将图像转换成灰度图像
plt.figure()  					# 新建一个图像 
plt.gray()  					# 不使用颜色信息 
plt.contour(im, origin='image')	# 在原点的左上角显示轮廓图像
plt.axis('equal')  
plt.axis('off')
#图像的直方图用来表征该图像像素值的分布情况。用一定数目的小区间（bin）来指定表征像素值的范围，每个小区间会得到落入该小区间表示范围的像素数目。该（灰度）图像的直方图可以使用hist() 函数绘制：
plt.figure()  
plt.hist(im.flatten(),128)  
plt.show() 





