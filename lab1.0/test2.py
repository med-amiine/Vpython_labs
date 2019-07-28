#exercice 3

l1 = [1,2,5]
l2 = [5,7,8]
res = [0,0,0]
list1 = []
list2 = []
operator =0
x = len(l1)-1
print ("lenght of list one ", x)
print('choose a number \n 1 : addition \n 2 : soustraction \n 3 : mutliplication \n 4: division')
op = input('[+] ')
op = int (op)
print (op)
def fplus(list1,list2,operator):
    for i in range (0,len(l1)):
        res[i] = l1[i] + l2[i]
        print (res)
def fminus(list1,list2,operator):
    for i in range (0,len(l1)):
        res[i] = l2[i] - l1[i]
        print (res)
def fmultipl(list1,list2,operator):
    for i in range (0,len(l1)):
        res[i] = l1[i] * l2[i]
        print (res)
def fdivision(list1,list2,operator):
    for i in range (0,len(l1)):
        res[i] = l1[i] / l2[i]
        print (res)
if op == 1 :
    fplus(l1,l2,op)
elif op == 2 :
    fminus(l1,l2,op)
elif op == 3 :
    fmultipl(l1,l2,op)
elif op == 4 :
    fdivision(l1,l2,op)
else :
    print ("error 404")
