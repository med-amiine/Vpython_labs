"""
* don't hit the wall
* __author__ = "Mohammed El Amine Idmoussi"
* build two walls using,generate a random number each time if its bigger than
  the one before go one step forward otherwise go one step back
  the maximum boundaries are (-9,15)
"""

import math
import random
import time


step = " "
nb = 10
hit = 0
temp = 0
val = 0

print("1", nb*step, "START", 11*step, "1")
print("1", nb*step, "0", 15*step, "1")
start = time.perf_counter()
while hit == 0:
    x = random.randint(-100, 100)
    # for debugging print("the next random number is: ", x)
    # time.sleep(1/4) slow down time of execution
    if x >= temp and nb < 25:
        # for debugging print("going on step forward.")
        nb = nb + 1
        temp = x
        val = val + 1
        d = 25-nb
        if val < 0:
            d = 25-nb-1
        print ("1", nb*step, val, d*step, "1")
    elif x <= temp and nb > 1:
        # for debugging print("going on step back.")
        nb = nb - 1
        temp = x
        val = val - 1
        d = 25-nb
        if val < 0:
            d = 25-nb-1
        print("1", nb*step, val, d*step, "1")

    else:
        hit = 1
        print("1", 10*step, "END", 13*step, "1")
t = time.perf_counter() - start
print("Time is : ", t)

#print(hit, sep=' ', end='', flush=True)
#a = "   indented string"
#leading_spaces = len(a) - len(a.lstrip())
#print(leading_spaces)