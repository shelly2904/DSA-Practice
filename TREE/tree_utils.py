class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class Queue(object):
    def __init__(self):
        self.arr = []
        self.front = 0
        self.rear = -1

    def push(self, data):
        self.arr.append(data)
        self.rear += 1

    def pop(self):
        if not self.arr:
            return False
        top = self.arr[self.front]
        del self.arr[self.front]
        return top


class Stack(object):
    def __init__(self):
        self.top = -1
        self.arr = []

    def push(self, key):
        self.top += 1
        self.arr.append(key)

    def pop(self):
        if self.top == -1:
            return False
        top_ele = self.arr[self.top]
        del self.arr[self.top]
        self.top -= 1
        return top_ele


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


def mindepth_call(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    if not root.left:
        return mindepth_call(root.right) + 1

    if not root.right:
        return mindepth_call(root.left) + 1

    return min(mindepth_call(root.left), mindepth_call(root.right)) + 1
