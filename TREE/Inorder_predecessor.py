from tree_questions import Node, inorder, Stack, Queue

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

def inorder_predecessor(root, key):
	key_node = search(root, key)
	parent = key_node.parent
	if parent:
		if parent.right == key_node:
			pred = key_node.left
			while pred.right:
				pred = pred.right
		else:
			pred = key_node.right
			while pred.left:
				pred = pred.left
	if not parent:
		pred = key_node.left
		while pred.right:
			pred = pred.right
	return pred.data


'''
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
'''	

def print_tree(root):
	if not root:
		return None 

	print_tree(root.left)
	print_tree(root.right)
	try:
		print "parent of ", root.data, " is ", root.parent.data
	except:
		pass


if __name__=="__main__":
	root = Node(1)
	root.left = Node(2)
	root.left.parent = root
	root.right = Node(3)
	root.right.parent = root
	root.left.left = Node(4)
	root.left.left.parent = root.left
	root.left.right = Node(5)
	root.left.right.parent = root.left
	root.left.right.left  = Node(6)
	root.left.right.left.parent = root.left.right
	root.left.right.right  = Node(7)
	root.left.right.right.parent = root.left.right
	root.left.right.right.left= Node(8)
	root.left.right.right.left.parent = root.left.right.right
	inorder(root)
	print
	print inorder_predecessor(root, 7)
	print 
	#print inorder_successor(root, 7)



