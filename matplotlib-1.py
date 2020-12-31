# plot a sine wave from 0 to 4pi  
import matplotlib.pyplot as plt
from numpy import *                      #也可以使用 from pylab import *  
plt.figure(figsize=(8,4))                    #创建一个绘图对象，大小为800*400
x_values = arange(0.0, math.pi * 4, 0.01)      #步长0.01，初始值0.0，终值4π 
y_values = sin(x_values)  
plt.plot(x_values,  y_values,  'b--',  linewidth=1.0, label='$sin(x)$') #进行绘图
plt. xlabel('x ')                             #设置X轴的文字
plt. ylabel('sin(x)')                          #设置Y轴的文字
plt.ylim(-1, 1)                             #设置Y轴的范围
plt. title('Simple plot')                       #设置图表的标题
plt.legend()                               #显示图例(legend)  
plt.grid(True)  
plt.savefig("sin.png")  
plt.show()  
 

 

