from collections import defaultdict
from typing import List


def singleNumber(nums: List[int]) -> List[int]:
    hashmap = defaultdict(lambda: 0)
    for i in nums:
        hashmap[i] = hashmap[i] + 1
    return [k for k,v in hashmap.items() if v ==1]


# print(singleNumber([1,2,1,3,2,5]))


def numIdenticalPairs(nums: List[int]) -> int:
    hashmap = dict()

    for i in nums:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    n_pairs = 0
    for k,v in hashmap.items():
        n = v
        if n > 1:
            n_pairs += (n*(n-1))/2

    return round(n_pairs)

print(numIdenticalPairs([1,1,1,1]))