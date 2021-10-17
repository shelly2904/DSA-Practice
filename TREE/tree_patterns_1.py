from tree_utils import *

"""
Check if a tree is balanced or not.
The difference between right subtree and left subtree is not greater than 1
"""


def check_balance(root):
    if not root:
        return False
    l_height = height(root.left)
    r_height = height(root.right)
    if abs(l_height - r_height) > 1:
        return False
    else:
        return True


"""
Calculate number of nodes in a tree
"""


def number_nodes(root):
    if not root:
        return 0
    return 1 + number_nodes(root.left) + number_nodes(root.right)


"""
Check if the tree is balanced till k
"""


def check_k_unbalance(root, k):
    if not root:
        return 0
    l_nodes = number_nodes(root.left)
    r_nodes = number_nodes(root.right)
    print(l_nodes, r_nodes)
    if abs(l_nodes - r_nodes) > k:
        if check_k_unbalance(root.left, k) and check_k_unbalance(root.right, k):
            return root.data
    return None


"""
Check if the tree is mirror image of itself
"""


def check_mirror(self, root):
    pre_arr = self.preorder(root)
    mid = len(pre_arr) / 2
    start = mid - 1
    end = mid + 1
    sym = True
    while start >= 0 and end < len(pre_arr):
        if pre_arr[start] == pre_arr[end]:
            start -= 1
            end += 1
            sym = True
        else:
            sym = False
            break

    if sym:
        return True
    else:
        return False


"""
Mirror image with recursion
"""


def check_mirror_recursion(self, root1, root2):
    if not root1 and not root2:
        return True
    elif root1 and root2:
        if root1.data == root2.data:
            if self.check_mirror_recursion(root1.left, root2.right) and self.check_mirror_recursion(root1.right,
                                                                                                    root2.left):
                return True
            else:
                return False
    else:
        return False


"""
MAIN FUNCTION
"""

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(4)
    root.right.right = Node(4)
    # root.left.left.right.right = Node(6)
    # root.left.left.right.right.left = Node(7)
    # print t.check_balance(root)
    # print t.check_k_unbalance(root, 1)
    print(check_mirror_recursion(root, root))
