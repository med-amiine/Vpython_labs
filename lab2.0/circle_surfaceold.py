"""
* circle surface with random hit
* __author__ = "Mohammed El Amine Idmoussi"
* imagine a circle inside a square how many random hit you need to fully cover all the circle surface
*
"""

import math
import random

d = 0
hit_circle = 0
hit_square = 0

sf_circle = [[] for _ in range(10 ** 6 + 1)]
div_pi = [[] for _ in range(10 ** 6 + 1)]
sf_square = 4

for i in range(1, 10 ** 6 + 1):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    d = (math.sqrt((x ** 2) + (y ** 2)))
    hit_square = i
    if d < 1:
        hit_circle += 1
    sf_circle[i] = 4 * (hit_circle / hit_square)
    div_pi[i] = sf_circle[i] / math.pi

f = open('myfile.txt', 'w')
for i in range(1, 10 ** 6 + 1):
    if i <= 100 or i == 10 ** 3 or i == 10 ** 4 or i == 10 ** 5 or i == 10 ** 6:
        f.write(str(i) + ')' + 'circle surface : ' + str(sf_circle[i]) + ' \n' + '  S/pi: ' + str(div_pi[i]) + ('\n'))
f.close()

print("You had hited the circle for", hit_circle, "times")
