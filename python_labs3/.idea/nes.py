import random
import time

step=10
tab=' '
wall = 0
temp=0
number = 0
print('|',tab*5,'START',(20-step)*tab,'|')
start = time.clock()
while(wall==0):
    a = random.randint(-10,10)
    if(a>=temp and step>0):
        step+=1
        temp = a
        number+=1
        print('|',tab*step,number,(20-step)*tab,'|')
    elif (a<temp and step<20) :
        step-=1
        temp = a
        number-=1
        print('|',tab*step,number,(20-step)*tab,'|')
    else:
        wall = 1

print ('Time required : ',time.clock()-start)
