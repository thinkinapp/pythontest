#折线图
import numpy as np  
import matplotlib.pyplot as plt 
# 本例中生成从 -10 到 10 的5个数
#  安装包  https://www.cnblogs.com/xiaoguan-bky/p/11184740.html
x = np.linspace(-10, 10, 5)  # linspace 用于生成等区间的一组数
y = x ** 2  
plt.plot(x, y, linestyle = "--")  # linestyle 设置线的类型，虚线： '--'
plt.show() 


