class Solution(object):
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


sol = Solution()
print(sol.twoSum([0,4,3,0], 0))