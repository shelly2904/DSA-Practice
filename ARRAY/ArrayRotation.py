#!/bin/python

# Complete the rotLeft function below.
def rotRight(a, d):
    n = len(a)
    # To get the starting point of rotated array 
    # mod = d % n
    newarr = [0]*n
    # Prints the rotated array from start position 
    for i in range(n): 
        newarr[(d + i) % n] = a[i]
    return newarr

def rot_right_inplace(a, d):
    a = list(reversed(a))
    a = list(reversed(a[:d])) + a[d:]
    a = a[:d] + list(reversed(a[d:]))
    return a

def rotLeft(a, d):
    n = len(a)
    # To get the starting point of rotated array 
    mod = d % n 
    newarr = [0]*n
    # Prints the rotated array from start position 
    for i in range(n): 
        newarr[i] = a[(d + i) % n]
    return newarr



if __name__ == '__main__':
    # nd = input().split()

    # n = int(nd[0])
    #
    # d = int(nd[1])

    # a = map(int, raw_input().rstrip().split())
    n = 7
    d = 3
    a = [1,2,3,4,5,6,7]
    #
    # resultLeft = rotLeft(a, d)
    # print("Rotate by left ", resultLeft)

    resultRight = rot_right_inplace(a, d)
    print("Rotate by right ", resultRight)
