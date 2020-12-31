#绘制图像
from PIL import Image  
from numpy import *
import matplotlib.pyplot as plt 
im = array(Image.open('d:\\test.jpg'))  # 读取图像到数组中  
plt.imshow(im)  # 绘制图像 
# 一些点  
x = [100,100,400,400]  
y = [200,500,200,500]  
# 使用红色星状标记绘制点  
plt.plot(x,y,'r*')  
# 绘制连接前两个点的线  
plt.plot(x[:2],y[:2])  
# 添加标题，显示绘制的图像  
plt.title('Plotting: " test.jpg"')
plt.axis('off') 
plt.show()



