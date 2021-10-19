"""
Find K smallest element in BST
"""


class Solution(object):
    def __init__(self):
        self.cnt = 0
        self.ans = 0

    def find_smallest(self, root, k):
        if root is None:
            return None
        self.find_smallest(root.left, k)
        self.cnt += 1
        if self.cnt == k:
            self.ans = root.val
        self.find_smallest(root.right, k)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        self.find_smallest(root, k)
        return self.ans
