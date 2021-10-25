from tree_utils import TreeNode
from tree_utils import Queue


class NodeTree:
    def __init__(self, val=0):
        self.val = val
        self.right = None
        self.left = None
        self.parent = None


def search(root, key):
    st = Queue()
    st.push(root)
    while st.arr:
        current = st.pop()
        if not current:
            continue
        if current.data == key:
            return current
        st.push(current.left)
        st.push(current.right)

# def inorder_predecessor(root, key):
#     key_node = search(root, key)
#     parent = key_node.parent
#     if parent:
#         if parent.right == key_node:
#             pred = key_node.left
#             while pred.right:
#                 pred = pred.right
#         else:
#             pred = key_node.right
#             while pred.left:
#                 pred = pred.left
#     if not parent:
#         pred = key_node.left
#         while pred.right:
#             pred = pred.right
#     return pred.data
#
#
def inorder_successor(root, key):
    key_node = search(root, key)
    parent = key_node.parent
    if parent:
        if parent.right == key_node:
            pred = key_node.right
            if pred:
                while pred.left:
                    pred = pred.left
            else:
                pred = key_node
        else:
            pred = key_node.left
            if pred:
                while pred.right:
                    pred = pred.right
            else:
                pred = key_node
    if not parent:
        pred = key_node.right
        if pred:
            while pred.left:
                pred = pred.left
        else:
            pred = key_node
    return pred.data


# def print_tree(root):
#     if not root:
#         return None
#
#     print_tree(root.left)
#     print_tree(root.right)
#     try:
#         print("parent of ", root.data, " is ", root.parent.data)
#     except:
#         pass


def find_min(root):
    if not root:
        return
    while root.left:
        root = root.left
    return root

def inorder_successor_bst(root, key):
    if not root:
        return
    succ = None
    curr = root

    while curr.val != key:
        if curr.val > key and curr.left:
            succ = curr
            curr = curr.left
        elif curr.right:
            curr = curr.right

    if curr and curr.right:
        succ = find_min(curr.right)

    return succ.val


if __name__ == "__main__":
    root = TreeNode(9)
    root.left = TreeNode(2)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(7)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(8)
    root.left.right.left.left = TreeNode(5)
    # inorder(root)
    # print
    # print(inorder_predecessor(root, 7))
    # print
    print(inorder_successor_bst(root, 9))
