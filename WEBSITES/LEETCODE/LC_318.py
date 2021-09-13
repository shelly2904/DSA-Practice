from typing import List


def countSetBits(n):
    # Stores the count
    # of set bits in n
    count = 0

    while n > 0:
        count += n & 1
        n >>= 1
    # Return the count
    return count

def maxProduct(words: List[str]) -> int:
    bits = [0] * len(words)

    for i in range(len(words)):
        for j in range(len(words[i])):
            bits[i] |= 1 << (ord(words[i][j]) - 97)

    result = 0
    for i in range(len(bits)):
        for j in range(len(bits)):
            if (bits[i] & bits[j]) == 0:
                L = countSetBits(bits[i])
                R = countSetBits(bits[j])
                result = max(L * R, result)

    print(result)



maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])