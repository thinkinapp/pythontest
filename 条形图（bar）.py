#条形图（bar）
import matplotlib.pyplot as plt
import numpy as np
y=[20,10,30,25,15,34,22,11]
x=np.arange(8)   #0---7
plt.bar(left=x,height=y,color='green',width=0.5)  #通过设置left来设置并列显示
plt.show()








