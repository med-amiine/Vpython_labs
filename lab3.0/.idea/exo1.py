import math
import random
import time


step = " "
nb = 10
hit = 0
temp = 0
val = 0

print ("1",nb*step,"START",11*step,"1")
print ("1",nb*step,"0",15*step,"1")
start = time.clock()
while (hit ==0):
    x = random.randint(-100,100)
    if x>= temp and nb<25:
        nb = nb +1
        temp = x
        val = val +1
        d = 25-nb
        if val<0 :
            d = 25-nb-1
        print ("1",nb*step,val,d*step,"1")
    elif x<=temp and nb>1:
        nb = nb -1
        temp = x
        val = val -1
        d = 25-nb
        if val<0 :
            d = 25-nb-1
        print ("1",nb*step,val,d*step,"1")

    else:
        hit=1
t = time.clock() - start
print ("Time is : ",t)

#print(hit, sep=' ', end='', flush=True)
#a = "   indented string"
#leading_spaces = len(a) - len(a.lstrip())
#print(leading_spaces)