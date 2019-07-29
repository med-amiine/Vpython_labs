"""
* probability of matching
* __author__ = "Mohammed El Amine Idmoussi"
*
"""


import numpy as np


def match(nb):

    j = 0

    while j < 5:
        n = 0
        a = np.random.randint(1,366,50)
        unique_elements,counts_elements = np.unique(a, return_counts=True)
        for i in counts_elements:
            x = counts_elements[i]
            if x >= nb:
                n = n + 1
        rate = n/counts_elements.size
        print(a)
        print(counts_elements)
        print(rate)
        j = j + 1
    print(n)

match(2)