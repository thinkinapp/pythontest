#饼状图
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] 		#指定默认字体  
plt.rcParams['axes.unicode_minus'] = False		#解决保存图像是负号'-'显示为方块的问题
labels = ["一季度", "二季度", "三季度", "四季度"]
facts = [25, 40, 20, 15]
explode = [0, 0.03, 0, 0.03]
# 设置显示的是一个正圆，长宽比为 1:1
plt.axes(aspect = 1)
# x为数据, 根据数据在所有数据中所占的比例显示结果
# labels设置每个数据的标签
# autoper 设置每一块所占的百分比
# explode 设置某一块或者很多块突出显示出来， 由上面定义的explode数组决定
# shadow 设置阴影，这样显示的效果更好
plt.pie(x = facts, labels = labels, autopct = "%.0f%%", explode= explode, shadow= True)
plt.show()
