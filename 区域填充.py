#区域填充
from PIL import Image  
import numpy as np
import matplotlib.pyplot as plt 

def Plot_Fill(Sim_T):
    x = np.arange(0, 1, 0.01)
    y = np.sin(x)

    fig = plt.figure()
    ax = plt.gca()
    ax.plot(x, y, color='red', linewidth=2)
    plt.vlines(Sim_T, [0], 1, color="green", linewidth=3, linestyles="dashed")
    ax.fill_betweenx(y, Sim_T, x, facecolor="orange", color="blue")
    ax.fill_betweenx(y, Sim_T, x, where=x >= Sim_T, facecolor='blue', color="blue")
    ax.set_title('S-curve of LSH')
    ax.annotate('T', xy=(1.03*Sim_T, 0.45))
    plt.grid()
    plt.savefig('LSH_Scurve.png')
    plt.show()
Plot_Fill(0.7)






