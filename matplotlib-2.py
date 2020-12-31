import math  
import matplotlib.pyplot as plt
y_values = []  
x_values = []  
num = 0.0  
#collect both num and the sine of num in a list  
while num < math.pi * 4:  
    y_values.append(math.sin(num))  
    x_values.append(num)  
    num += 0.1  
plt.plot(x_values,y_values,'r*')  
plt.show()  

 

