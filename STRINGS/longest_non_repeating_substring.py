from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        hashmap = defaultdict(int)
        max_len = 0
        count = 0
        start = 0

        for i in range(len(s)):
            if s[i] not in hashmap.keys() or hashmap[s[i]] < start:
                count += 1
            else:
                # import pdb; pdb.set_trace()
                start = hashmap[s[i]]
                count = i - start

            max_len = max(max_len, count)
            hashmap[s[i]] = i


        return max(max_len, count)


sol = Solution()
print(sol.lengthOfLongestSubstring("cdd"))
