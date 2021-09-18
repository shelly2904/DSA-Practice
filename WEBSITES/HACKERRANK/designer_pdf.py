#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    max_height = 0
    chars = 0
    for i in word:
        max_height = max(max_height, h[ord(i) - 97])
        chars += 1

    area = max_height*chars

    return area



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

    word = 'torn'

    result = designerPdfViewer(h, word)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
