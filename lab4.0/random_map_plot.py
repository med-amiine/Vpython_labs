"""
* random map plot
* __author__ = "Mohammed El Amine Idmoussi"
"""

import numpy as np
import matplotlib.pyplot as plt
import math

plt.rcParams['font.size'] = 18
plt.style.use('classic')

colorList = ['black', 'yellow', 'green', 'blue', 'red']
i = 0
for i in range(5):
    xList = []
    yList = []
    oldX = 0
    oldY = 0
    for j in range(10 ** 5):
        angle = np.random.uniform(0, 2 * np.pi)
        newX = math.cos(angle)
        newY = math.sin(angle)

        xList.append(oldX + newX)
        yList.append(oldY + newY)

        oldX = oldX + newX
        oldY = oldY + newY

    plt.plot(xList, yList, '-', color=colorList[i], zorder=i + 1)
    plt.plot(oldX, oldY, 'D', color=colorList[4 - i], zorder=i + 1)
plt.show()
