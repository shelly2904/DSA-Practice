class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(0, rows):
            for j in range(i+1, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        left, right = 0, cols - 1
        while left <= right:
            for i in range(0, rows):
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1

        return matrix


sol = Solution()
print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]))