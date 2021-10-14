
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


"""
Minimum window substring
"""

from collections import defaultdict

def minimum_substring(string, pat):

    hash_map = defaultdict(int)
    cnt = 0
    n = len(string)

    for i in pat:
        hash_map[i] += 1
        if hash_map[i] == 1:
            cnt += 1

    i = 0
    j = 0
    start = 0
    ans = len(string) + 1

    while j < len(string):
        hash_map[string[j]] -= 1

        if hash_map[string[j]] == 0:
            cnt -= 1
            while cnt == 0:
                print(hash_map, cnt, ans, start)
                if j-i+1 < ans:   # get the minimum list
                    ans = j-i+1
                    start = i

                hash_map[string[i]] += 1
                if hash_map[string[i]] > 0:
                    cnt += 1
                i += 1
        j += 1

    return string[start:start+ans]

"""
MAximum of all subarrays of size k
"""
def max_subarray(arr, k):
    n = len(arr)

    max_ele = -sys.maxsize - 1

    max_arr = []
    i = 0
    j = 0
    while j < n:
        max_ele = max(max_ele, arr[j])

        if j -i + 1 == k:
            max_arr.append(max_ele)
            i += 1
            j = i
        else:
            j += 1

    return max_arr

print(max_subarray([1,3,-1,4,5,1,2], 3))



# print(minimum_substring("abaacbabac", "abc"))



#print(count_anagrams("aabaaabaa", "aaba"))
#print(first_neg_k([-8,2,3,-6,10], 2))
#print(max_sub_k([2,5,1,8,2,9,1], 3))

