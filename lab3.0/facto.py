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

