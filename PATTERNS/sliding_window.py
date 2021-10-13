
"""
Fixed Sliding window
"""
import sys

"""
Maximum/Minimum of k-size sub-array
"""


def max_sub_k(arr, k):
    i = 0
    j = i+1

    max_sum = -sys.maxsize - 1

    while j < len(arr):
        if j-i+1 < k:
            j += 1

        if j - i + 1 == k:
            max_sum = max(max_sum, sum(arr[i:j+1]))
            i += 1
            j = i+1

    return max_sum


"""
First Negative Integer in every window of size k
"""
from collections import deque
def first_neg_k(arr, k):
    n = len(arr)

    ans = []

    queue = deque()
    for i in range(k-1):
        if arr[i] < 0:
            queue.append(arr[i])

    for i in range(k-1, n):
        if arr[i] < 0:
            queue.append(arr[i])
        if queue:
            ans.append(queue[0])
            if queue[0] == arr[i-k+1]:
                queue.pop()
        else:
            ans.append(0)

    return ans



"""
Count of occurences of Anagrams
"""

from collections import defaultdict
from copy import deepcopy
def count_anagrams(string, pat):

    hash_map = defaultdict(int)
    k = len(pat)  # window size
    n = len(string)

    cnt = 0

    for i in pat:
        hash_map[i] += 1

    i = 0
    j = 0

    temp_hashmap = deepcopy(hash_map)
    while j < n:
        temp_hashmap[string[j]] -= 1
        if j - i + 1 < k:
            j += 1
            continue
        if j - i + 1 == k:
            if list(set(temp_hashmap.values()))[0] == 0:
                cnt += 1
                temp_hashmap = deepcopy(hash_map)

            i += 1
            j = i

    return cnt

print(count_anagrams("aabaaabaa", "aaba"))


#print(first_neg_k([-8,2,3,-6,10], 2))
#print(max_sub_k([2,5,1,8,2,9,1], 3))

