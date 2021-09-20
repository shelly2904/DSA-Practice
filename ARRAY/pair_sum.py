class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        from collections import defaultdict

        hashmap = defaultdict(int)

        for i in range(0, len(nums)):
            if hashmap[target - nums[i]] != 0:
                return [i, nums.index(target - nums[i])]
            hashmap[nums[i]] = 1

        return []


# sol = Solution()
# print(sol.twoSum([0,4,3,0], 0))


# 3Sum
from collections import defaultdict

class Solution(object):

    def twoSum(self, prev_target, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = defaultdict(int)

        for i in range(0, len(nums)):
            if hashmap[target - nums[i]] != 0:
                if prev_target not in [i+1, nums.index(target - nums[i]) + 1]:
                    return [i+1, nums.index(target - nums[i]) + 1]

            hashmap[nums[i]] = 1

        return []

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        for i in range(0, len(nums) - 1):
            values = self.twoSum(i, nums[i + 1:], -nums[i])
            if values and sum([nums[i], nums[values[0]], nums[values[1]]]) == 0:
                results.append(sorted([nums[i], nums[values[0]], nums[values[1]]]))
        return results


sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))