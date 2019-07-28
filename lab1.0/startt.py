#exercice 1
l = [1,5,10,15,20]
somme = 0
prod = 1
i=0
x = len(l)-1
for i in l:
    somme = somme + i
    if i==l[x]:
     print ("sum is",somme)

for i in l:
    prod = prod * i
    if i==l[x]:
     print ("produc is",prod)

