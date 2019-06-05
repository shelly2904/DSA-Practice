#!/bin/python

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotRight(a, d):
    n = len(a)
    # To get the starting point of rotated array 
    mod = d % n 
    newarr = [0]*n
    # Prints the rotated array from start position 
    for i in range(n): 
        newarr[(mod + i) % n] = a[i]
    return newarr


def rotLeft(a, d):
    n = len(a)
    # To get the starting point of rotated array 
    mod = d % n 
    newarr = [0]*n
    # Prints the rotated array from start position 
    for i in range(n): 
        newarr[i] = a[(mod + i) % n]
    return newarr


if __name__ == '__main__':
    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    resultLeft = rotLeft(a, d)
    print "Rotate by left ", resultLeft 

    resultRight = rotRight(a, d)
    print "Rotate by right ", resultRight 
