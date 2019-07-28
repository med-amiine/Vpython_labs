"""
* list sum and prod
* __author__ = "Mohammed El Amine Idmoussi"
* before numpy
"""

l = [3]
somme = 0
prod = 1
i=0
x = len(l)-1
n = int(input("whats the size of your list :"))

for i in range(0, n):
    ele = int(input())
    l.append(ele)

for i in l:
    somme = somme + i
    if i==l[x]:
     print ("sum is",somme)

for i in l:
    prod = prod * i
    if i==l[x]:
     print ("produc is",prod)

