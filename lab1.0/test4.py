#exercice 2
nb = input('type a number:')
nb = int (nb)
print (nb)

check = 0;
if nb > 1:
    # check for factors
    for i in range(2,nb):
        if (nb % i) == 0 :
            print("this",nb,"is not prime ")
            check = 1
            break
    else:
        print(nb,"is a prime number")
        check = 0

if check == 1 :
    if (nb % 2) == 0 :
        print(nb,"is a even number")
    else:
        print("this",nb,"is odd")








