import sys
sys.setrecursionlimit(10000000)


class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class Tree(object):
	def __init__(self, inarr, prearr):
		self.inarr = inarr
		self.prearr = prearr
		self.n = len(prearr)

	def postorder(self, root):
		self.postorder(root.left)
        self.postorder(root.right)
        print root.data



	def create_subarray(self, P, I):
		#print "Printing the preorder: ", P
		#print "Printing the inorder: ", I
		if len(P) == 1:
			#print "Element is ", P[0]
			return Node(P[0])
		node = P[0]
		
		n_idx = I.index(node)
		root = Node(node)
		#print "Node is : ", node
		left = self.create_subarray(P[1:n_idx+1], I[0:n_idx])
		right = self.create_subarray(P[n_idx+1:], I[n_idx+1:])
		root.left, root.right = left, right 
		return root




if __name__ == '__main__':
	preorder = [1, 2, 4, 5, 3, 6, 7]
	inorder = [4, 2, 5, 1, 6, 3, 7]

	tree = Tree(inorder, preorder)
	tree.root = tree.create_subarray(preorder,inorder)
	print "post orfer tree: " 
	tree.postorder(tree.root)
	