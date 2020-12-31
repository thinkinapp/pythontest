#区域填充
from PIL import Image  
import numpy as np
import matplotlib.pyplot as plt 

def Plot_LSH_Curve(b, r, Sim_T):
    s = np.arange(0, 1, 0.01)
    p = 1 - np.power(1 - np.power(s, r), b)

    fig = plt.figure()
    ax = plt.gca()
    ax.plot(s, p, color='red', linewidth=2)
    plt.vlines(Sim_T, [0], 1, color="green", linewidth=3, linestyles="dashed")
    ax.fill_betweenx(p, Sim_T, s, facecolor="orange", color="blue")
    ax.fill_betweenx(p, Sim_T, s, where=s >= Sim_T, facecolor='blue', color="blue")
    ax.set_title('S-curve of LSH')
    ax.annotate('T', xy=(1.03*Sim_T, 0.45))
    plt.grid()
    plt.savefig('LSH_Scurve.png')
    plt.show()
Plot_LSH_Curve(2.2, 1.5, 0.7)






