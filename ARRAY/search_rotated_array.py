class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        if low == high and nums[low] == target:
            return low

        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[high]:
                if target <= nums[mid] and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target >= nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


sol = Solution()
print(sol.search([1,3], 3))