class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.parent = None



class Queue(object):
	def __init__(self):
		self.arr= []
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
		print current.data
		current = current.right
		while current:
			S.push(current)
			current = current.left

def height(root):
	if not root:
		return 0
	return 1+ max(height(root.left), height(root.right))



def print_levelwise(root):
	Q = Queue()
	Q.push(root)
	while True:
		nodeCount = len(Q.arr)
		if nodeCount == 0:
			break
		while nodeCount > 0:
			current = Q.pop()
			print current.data, " ",
			if current.left:
				Q.push(current.left)
			if current.right:
				Q.push(current.right)
			nodeCount -=  1
		print

if __name__=="__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.left.right.right = Node(6)
	#inorder_without_recursion(root)
	print_levelwise(root)





