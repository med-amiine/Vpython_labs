"""
* even - odd - prime
* __author__ = "Mohammed El Amine Idmoussi"
"""


nb_input = int(input('type a number:'))
print(nb_input)


def simple(nb):
    print("According to simple algo:")
    if nb > 1:
        for i in range(2,nb):
            if (nb % 2) == 0:
                print("this number", nb, "is even")
                break
            elif(nb % i) == 0:
                print("this number", nb, "is odd")
                break
            else:
                print("this number", nb, "is prime")
                break


def prime_even_odd(nb):
    print("According to prime_even_odd:")
    check = 0
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

    if check == 1:
        if (nb % 2) == 0 :
            print(nb,"is a even number")
        else:
            print("this",nb,"is odd")


simple(nb_input)
print("\n###############################\n")
prime_even_odd(nb_input)
