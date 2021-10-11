# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import sys


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        # root -> left -> right
        stack = []

        root = TreeNode(preorder[0])
        p = root
        i = 1
        top = -1

        stack.append(root)

        while i < len(preorder):
            top_val = stack[top].val if len(stack) > 0 else sys.maxsize
            if preorder[i] < p.val:
                node = TreeNode(preorder[i])
                p.left = node
                stack.append(p)
                p = node
                i += 1
            elif preorder[i] > p.val and preorder[i] <= top_val:
                node = TreeNode(preorder[i])
                p.right = node
                p = node
                i += 1
            else:
                p = stack.pop()

        return root


def construct_tree_from_traversals()

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

arr = [8,5,1,7,10,12]

sol = Solution()
root = sol.bstFromPreorder(arr)
inorder(root)

