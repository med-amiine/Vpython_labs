import numpy as np
import math
import random
import time


start = time.clock()
file = open("res.txt", "w")
for a in range (1,100):
    for b in range (1,100):
        for c in range (1,100):
            if (a**2+b**2==c**2):
                file.write('a**2 :'+ str(a)+'\t'+'b :'+str(b)+'\t'+'c :'+str(c)+'\n')
for a in range (1,100):
    for b in range (1,100):
        for c in range (1,100):
            if (a**3+b**3==c**3):
                   file.write('a**3 :'+ str(a)+'\t'+'b :'+str(b)+'\t'+'c :'+str(c)+'\n')

for a in range (1,100):
    for b in range (1,100):
        for c in range (1,100):
            if (a**4+b**4==c**4):
                file.write('a**4 :'+ str(a)+'\t'+'b :'+str(b)+'\t'+'c :'+str(c)+'\n')

for a in range (1,100):
    for b in range (1,100):
        for c in range (1,100):
            if (a**5+b**5==c**5):
                file.write('a**5 :'+ str(a)+'\t'+'b :'+str(b)+'\t'+'c :'+str(c)+'\n')
file.close()


