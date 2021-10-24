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


from collections import defaultdict, deque, OrderedDict
def vertical_order_traversal(root):
    if not root:
        return []

    queue = deque()
    v_node = defaultdict(list)
    hd_node = defaultdict(int)

    queue.append(root)
    hd_node[root] = 0
    v_node[0] = [root.data]

    while queue:
        curr = queue.popleft()
        if curr.left:
            queue.append(curr.left)
            hd_node[curr.left] = hd_node[curr] - 1
            hd = hd_node[curr.left]
            v_node[hd].append(curr.left.data)

        if curr.right:
            queue.append(curr.right)
            hd_node[curr.right] = hd_node[curr] + 1
            hd = hd_node[curr.right]
            v_node[hd].append(curr.right.data)

    sorted_m = OrderedDict(sorted(v_node.items()))
    return list(sorted_m.values())


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    # inorder_without_recursion(root)
    #print_levelwise(root)

    print(vertical_order_traversal(root))
