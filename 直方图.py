# 概率分布直方图 ，本例是标准正态分布  
import matplotlib.pyplot as plt
import numpy as np
mu=100   		# 设置均值，中心所在点
sigma=20  		# 用于将每个点都扩大响应的倍数
# x中的点分布在 mu 旁边，以mu为中点  
x=mu+sigma*np.random.randn(20000)# 随机样本数量20000
# bins 设置分组的个数100（显示有100个直方） 
plt.hist(x,bins=100,color='green',normed=True) 
plt.show()







