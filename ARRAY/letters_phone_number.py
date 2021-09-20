class Solution(object):

    def permute(self, digits, index):
        index = int(index)
        curr_idx = int(digits[index])
        char_map = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        if index > len(digits) - 1:
            return []

        if index == len(digits) - 1:
            return [i for i in char_map[curr_idx]]

        return [i + j for i in char_map[curr_idx] for j in self.permute(digits, index + 1)]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []

        return self.permute(digits, 0)



sol = Solution()
print(sol.letterCombinations("23"))