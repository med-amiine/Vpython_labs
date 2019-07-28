import math
import random
import numpy as np


pi = math.pi
def facto(n):
    x = math.sqrt(math.pi)/2
    res = 1
    if n == 1:
        res = math.sqrt(pi)/2
        return res
    if n > 2:
        a = np.array(3,n,2)
        a = 1/2 * a
        for i in range(len(a)):
            res = res * i
    return res


def volume(nd):
    pi = math.pi
    v = (pi**(nd/2))/facto(nd)
    return v


v_math = 0
v_sphere = 0
rest = 0
hit = 0
x = 0

for j in range(2, 19):
    v_square = np.power(2, j)
    hit = 0
    for i in range(1, 10**6):
        x = np.random.uniform(-1, 1, j)
        x = np.power(x, 2)
        result = np.sum(x)
        if result <= 1:
            hit += 1
        v_math = volume(j)
        v_sphere = (v_square * hit)/i
        rest = v_sphere/v_math
print("ND" + ')    ' + "Vsimulation"+'    ' + "Vmath"+'     ' + "Vsimulation/Vmath" + '   '+"nb hit" + '\n)')
print(str(j) + ')    ' + str(v_sphere)+'    ' + str(v_math)+'     ' + str(rest) + '   '+str(hit) + '\n)')
