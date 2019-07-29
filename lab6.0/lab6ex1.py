import matplotlib.pyplot as plt
import random

plt.rcParams['font.size'] = 15
plt.style.use('classic')

x = 0
y = 0
x1=0
y1=0
p = 0
list_x = []
list_y = []
list_x1 = []
list_y1 = []

for i in range(10**6):
    p = random.randint(0, 101)
    if p == 1:
        x1 = 0
        y1 = 0.16 * y
    elif 1 < p <= 8:
        h = random.randint(0, 101)
        if h < 50:
            x1 = 0.2 * x - 0.26 * y
            y1 = 0.23 * x + 0.22 * y + 1.6
        else:
            x1 = -0.15 * x + 0.28 * y
            y1 = 0.26 * x + 0.24 * y + 0.44
    elif 8 < p < 85:
        x1 = 0.85 * x + 0.04 * y
        y1 = -0.04 * x + 0.85 * y + 1.6

    list_x.append(x1)
    list_y.append(y1)
    x = x1
    y = y1

print(list_x)
print(list_y)

plt.plot(list_x, list_y, ',', color='dodgerblue')
plt.show()
print("zooooooooooooooooooom")
#secend part


