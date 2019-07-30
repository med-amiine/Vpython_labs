import random

n = int(input())
temp = 0
for j in range(n):
    for i in range(10):
        x = random.randint(0, 1000)
        print(x, "", end="")
        if i == 0:
            temp = x
    print("\n")
for k in range(n):
    for i in range(10):
        y = random.randint(0, 1000)
        if k == 0 and i == 0:
            print(temp, "", end="")
        else:
            print(y, "", end="")
    print("\n")
