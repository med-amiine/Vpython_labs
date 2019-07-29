"""
* from random to identity matrix
* __author__ = "Mohammed El Amine Idmoussi"
*[ True False False False False]
 [False  True False False False]
 [False False  True False False]
 [False False False  True False]
 [False False False False  True]
"""

import numpy as np
import math
import random

year = 365

N = 5
X = 0
k = np.array([])
for j in range(101):
    for i in range(year + 2):
        A = np.random.randint(2, year, N)
        B = A.copy()
        B = B[:, np.newaxis]
        # if A match B we print True
        k = (A == B)
        print(k)
    # k = k - np.identity(i)
    # print(i+"prob =",np.sum(k)/100)
