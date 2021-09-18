def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    j = 0
    for i in range(0, len(nums) - 1):
        if nums[i] != nums[i + 1]:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    nums[j] = nums[len(nums) - 1]
    j += 1
    return nums[:j]
# print(removeDuplicates([1,1,2,2, 2,3,3, 4,5,6]))


def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    last_ele = s[0]

    i = len(s) - 1
    j = 0
    while (i >= 0 and j < i-1):
        print(i, j, s)
        s[j], s[i] = s[i], s[j]
        i -= 1
        j += 1

    return s

# print(reverseString(["h", "e", "l", "l", "o"]))

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        reversed_int = 0
        neg = 1 if x < 0 else 0
        x = (-1 * x) if x < 0 else x

        while x != 0:
            reversed_int = (reversed_int * 10) + (x % 10)
            x = x // 10

        if reversed_int > pow(2, 31) - 1:
            return 0

        if neg == 1:
            return -1 * reversed_int
        return reversed_int


sol = Solution()
print(sol.reverse(-123))