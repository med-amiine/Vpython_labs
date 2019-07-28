import numpy as np
import math
import random
import collections
count = 0

A = np.array([1,2,6,4,5,6,6,6])
B = np.array([1,2,6,4,5,6,6,6])
B = B[ : , np.newaxis]
#fe = np.identity([])
#print (A+B)
#print (A-B)
#print (A>B)
#print(A==B)
print(A==B)
K = A==B
K = K - np.identity()
#print(np.sum(A==B))
#print()

