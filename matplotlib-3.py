import matplotlib.pyplot as plt
for idx, color in enumerate("rgbyck"):
    plt.subplot(321+idx, facecolor=color)
plt.show()
