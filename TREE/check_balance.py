class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class Tree(object):
	def __init__(self):
		pass


	def height(self, root):
		if not root:
			return 0
		return 1+ max(self.height(root.left), self.height(root.right))

	def check_balance(self, root):
		if not root:
			return False
		l_height = self.height(root.left)
		r_height = self.height(root.right)
		if abs(l_height - r_height) > 1:
			return False
		else:
			return True


if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.left.right = Node(5)
	t = Tree()
	print t.check_balance(root)