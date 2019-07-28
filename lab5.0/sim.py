from __future__ import division
#import math
import numpy as np



#a = np.random.random_integers(1,5,10)
#print a
#x = np.bincount(a)
#print a[1]

#unique_elements,counts_elements = np.unique(a, return_counts=True)
#print("Frequency of unique values of the said array:")
#print counts_elements.size


def bdMatch(nb):

    j = 0

    while j < 5:
        n = 0
        a = np.random.random_integers(1,366,50)
        unique_elements,counts_elements = np.unique(a, return_counts=True)
        for i in counts_elements:
            x = counts_elements[i]
            if x >=nb:
                n = n + 1
        rate = n/counts_elements.size
        print(a)
        print(counts_elements)
        print(rate)
        j = j + 1
    print(n)

bdMatch(2)