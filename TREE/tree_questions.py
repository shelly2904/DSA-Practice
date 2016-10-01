class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class Stack(object):
	def __init__(self):
		self.top = -1
		self.arr = []

	def push(self, key):
		self.top += 1
		self.arr.append(key)

	def pop(self):
		if self.top == -1:
			print "Under flow"
			return False
		top_ele = self.arr[self.top]
		del self.arr[self.top]
		self.top -= 1
		return top_ele



#to check whether a tree is complete binary tree or not
def check_complete(root):
	if root == None:
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


def inorder(root):
	if not root:
		return None

	inorder(root.left)
	print root.data
	inorder(root.right)


if __name__=="__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	#print check_complete(root)
	#print LCA(root, 4, 5)
	print inorder(root)





