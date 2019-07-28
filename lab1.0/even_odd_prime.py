#exercice 2
nb = input('type a number:')
nb = int (nb)
print (nb)
if nb > 1:
    for i in range(2,nb):
        if (nb % 2)==0:
            print("this",nb,"is even")
            break
        elif(nb % i) == 0:
            print("this",nb,"is odd")
            break
        else:
            print("this",nb,"is prime")
            break

