from tree_utils import *

"""
Find the lowest common ancestor
"""


def LCA(root, n1, n2):
    if not root:
        return False
    if root.data == n1 or root.data == n2:
        return root.data
    left = LCA(root.left, n1, n2)
    right = LCA(root.right, n1, n2)
    if left and right:
        return root.data
    if left:
        return left
    else:
        return right


"""
Print all ancestors
"""


def print_all_ancestors(root, key):
    if not root:
        return False
    if key == root.data:
        return True
    if print_all_ancestors(root.left, key) or print_all_ancestors(root.right, key):
        print(root.data)
        return True


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    key = 3
    print_all_ancestors(root, key)
