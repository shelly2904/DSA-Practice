from tree_utils import *

"""
to check whether a tree is complete binary tree or not
"""


def check_complete(root):
    if root is None:
        return False
    stack = Stack()
    stack.push(root)
    flag = True
    while len(stack.arr) > 0:
        el = stack.pop()
        if not el.left and el.right:
            flag = False
            return False

        if not el.left and not el.right:
            flag = True

        if el.left:
            stack.push(el.left)

        if el.right:
            stack.push(el.right)
    if flag:
        return True
    else:
        return False


"""
find the lowest common ancestor
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