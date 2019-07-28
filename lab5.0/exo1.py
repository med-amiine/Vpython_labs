import numpy as np
import math
import random

year = 365

N = 5
X = 0
k = np.array([])
for j in range(101):
        for i in range(year+2):
            A = np.random.randint(2,year,N)
            B = A.copy()
            B = B[ : , np.newaxis]
            k = (A==B)
            print(A==B)
           # k = k - np.identity(i)
            #print(i+"prob =",np.sum(k)/100)


