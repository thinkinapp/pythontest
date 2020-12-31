#散点图
import matplotlib.pyplot as plt  
import numpy as np  
# 产生100到200的10个随机整数
x = np.random.randint(100, 200, 10)  
y = np.random.randint(100, 130, 10)
# x指x轴 ，y指y轴  
# s设置显示的大小，指的是面积  ， c设置显示的颜色  
# marker设置显示的形状, "o"  是圆，"v"向下三角形，"v"向上三角形，所有的类型：http://matplotlib.org/api/markers_api.html?highlight=marker#module-matplotlib.markers
# alpha 设置点的透明度  
plt.scatter(x, y, s= 100, c= "r", marker= "v", alpha= 0.5) # 绘制图形 
plt.show() # 显示图形








