from tree_utils import *

def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.data)
    inorder(root.right)


def inorder_without_recursion(root):
    S = Stack()
    current = root
    S.push(current)
    current = current.left
    while current:
        S.push(current)
        current = current.left
    while S.arr:
        current = S.pop()
        print(current.data)
        current = current.right
        while current:
            S.push(current)
            current = current.left


def print_levelwise(root):
    Q = Queue()
    Q.push(root)
    while True:
        nodeCount = len(Q.arr)
        if nodeCount == 0:
            break
        while nodeCount > 0:
            current = Q.pop()
            print(current.data, " ", )
            if current.left:
                Q.push(current.left)
            if current.right:
                Q.push(current.right)
            nodeCount -= 1
        print()


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    # inorder_without_recursion(root)
    print_levelwise(root)
