"""
* addition - subtraction - multiplication - division
* __author__ = "Mohammed El Amine Idmoussi"
* list operation , before Numpy
"""


first_list  = [1, 2, 5]
second_list = [5, 7, 8]
res = [0, 0, 0]
# list1 = []
# list2 = []
operator =0
x = len(first_list)-1
print("length of list one ", x)
print('choose a number \n 1 : addition \n 2 : subtraction \n 3 : multiplication \n 4: division')
op_input = input('[+] ')
op_input = int(op_input)
print(op_input)


def fplus(l1, l2):
    for i in range (0,len(l1)):
        res[i] = l1[i] + l2[i]
    print("Result : ", res)


def fminus(l1, l2):
    for i in range(0, len(l1)):
        res[i] = l2[i] - l1[i]
    print("Result : ", res)


def fmultipl(l1, l2):
    for i in range(0,len(l1)):
        res[i] = l1[i] * l2[i]
    print("Result : ", res)


def fdivision(l1, l2):
    for i in range(0, len(l1)):
        res[i] = l1[i] / l2[i]
    print("Result : ", res)


def operation_handler(op, list1, list2):
    if op == 1:
        fplus(list1, list2)
    elif op == 2:
        fminus(list1, list2)
    elif op == 3:
        fmultipl(list1, list2)
    elif op == 4:
        fdivision(list1, list2)
    else:
        print("error 404")


operation_handler(op_input, first_list, second_list)
