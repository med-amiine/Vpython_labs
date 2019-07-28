import numpy as np
import math
import random

year = 365

N = 0
i = 0
for i in range (101):
    rand = np.random.randint(2,year,i)
    for k in range(2,i):
         for j in range(i):
               if rand[i] == rand[j]:
                   k = rand[i]
                   count =+1

