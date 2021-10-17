from tree_utils import *

#to check whether a tree is complete binary tree or not
def check_complete(root):
	if root is None:
		return False
	stack = Stack()
	stack.push(root)
	flag = True
	while len(stack.arr) > 0:
		el =  stack.pop()
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

#find the lowest common ancestor
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







