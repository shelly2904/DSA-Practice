"""
LC: 11

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        water_trapped = 0
        length = len(height)
        i, j = 0, length - 1

        while i < j:
            water_trapped = max(water_trapped, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return water_trapped


sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
