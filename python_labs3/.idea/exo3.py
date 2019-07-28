import numpy as np
import math
import random
import time


exit = 'true'
i = 0
x = random.randint(0,10)
print (x)
print("guess a number between 1 and 10 \n")
start = time.clock()
while(exit== 'true'):
    nb = int(input("what is your guess : "))
    if (nb == x):
        print ("yes")
        exit = 'false'
        i=i+1
    else:
        i= i+1
t = time.clock() - start
print ("number of the attempt : ",i)
print ("Time of the sequence : ",t)