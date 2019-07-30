"""
* Zooming on a leaf
* __author__ = "Mohammed El Amine Idmoussi"
* plot and Zoom on a particular leaf
"""

import matplotlib.pyplot as plt
import random

plt.rcParams['font.size'] = 15
plt.style.use('classic')

max_x = 3.580
min_x = 1.580

min_y = 1.580
max_y = 3.828

x = 0
y = 0
x1 = 0
y1 = 0
p = 0
list_x = []
list_y = []
list_x1 = []
list_y1 = []

for i in range(1000):
    p = random.randint(0, 101)
    if p == 1:
        x2 = 0
        y2 = 0.16 * y
    elif 1 < p <= 7:
        h = random.randint(0, 101)
        if h < 50:
            x2 = 0.2 * x - 0.26 * y
            y2 = 0.23 * x + 0.22 * y + 1.6
        else:
            x2 = -0.15 * x + 0.28 * y
            y2 = 0.26 * x + 0.24 * y + 0.44
    elif 7 < p < 85:
        x2 = 0.85 * x + 0.04 * y
        y2 = -0.04 * x + 0.85 * y + 1.6

    if min_x < x2 < max_x and min_y < y2 < max_y:
        list_x1.append(x2)
        list_y1.append(y2)
        x = x2
        y = y2

print(list_x1)
print(list_y1)

plt.plot(list_x1, list_y1, ',', color='dodgerblue')
plt.show()
print("zooooooooooooooooom")

