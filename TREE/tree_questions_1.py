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

def height(root):
	if not root:
		return 0
	return 1+ max(height(root.left), height(root.right))


def print_all_ancestors(root, key):
	if not root:
		return False

	if key == root.data:
		return True
	if print_all_ancestors(root.left, key) or print_all_ancestors(root.right, key):
		print root.data,
		return True
 

if __name__=="__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.left.right.right = Node(6)
	key = 3
	print_all_ancestors(root, key)





