#箱形图
import numpy as np  
import matplotlib.pyplot as plt  
np.random.seed(100)  
data = np.random.normal(size = (1000, ), loc = 0, scale= 1) # 生成一组随机数，数量为1000  
# sym 调整好异常值的点的形状  
# whis 默认是1.5， 通过调整它的竖直来设置异常值显示的数量，  
# 如果想显示尽可能多的异常值，whis设置很小，否则很大  
plt.boxplot(data, sym ="o", whis = 1.5)  
# plt.boxplot(data, sym ="o", whis = 0.01)  
plt.show() 

