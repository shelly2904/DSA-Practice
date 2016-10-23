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

	def number_nodes(self, root):
		if not root:
			return 0
		return 1 + self.number_nodes(root.left) + self.number_nodes(root.right)

	def check_k_unbalance(self, root, k):
		if not root:
			return 0
		l_nodes = self.number_nodes(root.left)
		r_nodes = self.number_nodes(root.right)
		print l_nodes, r_nodes
		import pdb; pdb.set_trace()
		if abs(l_nodes - r_nodes) > k:
			if self.check_k_unbalance(root.left, k) and self.check_k_unbalance(root.right, k):
				return root.data
		return None


	def inorder(self, root, a = []):
		if root:
			self.inorder(root.left)
			a.append(root.data)
			self.inorder(root.right)
			return a


	def check_mirror(self, root):
		pre_arr = self.preorder(root)
		mid = len(pre_arr)/2
		start = mid - 1
		end = mid + 1
		sym = True
		while start >= 0 and end < len(pre_arr):
			if pre_arr[start] == pre_arr[end]:
				start -= 1
				end += 1
				sym = True
			else:
				sym = False
				break

		if sym:
			return True
		else:
			return False


	def check_mirror_recursion(self, root1, root2):
		if not root1 and not root2:
			return True
		elif root1 and root2:
			if root1.data == root2.data: 
				if self.check_mirror_recursion(root1.left, root2.right) and self.check_mirror_recursion(root1.right, root2.left):
					return True
				else:
					return False
		else:
			return False







if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(2)
	root.left.left = Node(4)
	root.right.right = Node(4)
	#root.left.left.right.right = Node(6)
	#root.left.left.right.right.left = Node(7)
	t = Tree()
	#print t.check_balance(root)
	#print t.check_k_unbalance(root, 1)
	print t.check_mirror_recursion(root, root)