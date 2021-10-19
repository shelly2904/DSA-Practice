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
            return flag

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


"""
K-th ancestor of a node
1. We can compute the ancestor of each node by traversing through level wise
2. Next we iterate through  the hashmap and check if k == cnt
"""

from collections import defaultdict, deque

def kth_ancestor(root, node, k):

    hashmap = defaultdict(int)
    hashmap[root.data] = -1
    queue = deque()
    queue.append(root)

    while queue:
        n = queue.popleft()
        if n.left:
            hashmap[n.left.data] = n.data
            queue.append(n.left)
        if n.right:
            hashmap[n.right.data] = n.data
            queue.append(n.right)
    cnt = 0
    while node != -1:
        node = hashmap[node]
        cnt += 1
        if cnt == k:
            return node

    return -1












# def kth_ancestor(root, node, k):
#     if not root:
#         return None
#     if root.data == node or (kth_ancestor(root.left, node, k) or kth_ancestor(root.right, node, k)):
#         print(root.data)
#         if k > 0:
#             k -= 1
#         elif k == 0:
#             print(root.data)
#             return None
#         return root


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    key = 3
    # print_all_ancestors(root, key)
    print(kth_ancestor(root, 6, 1))
