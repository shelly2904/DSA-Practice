class TreeNode:
	def __init__(self, data):
		self.data = data
		self.children = []
		self.parent = None 


	def add_child(self, child):
		child.parent = self  #set parent
		self.children.append(child)  



def build_tree():
	root = TreeNode("Electronics")
	
	laptop = TreeNode("Laptop")
	laptop.add_child(TreeNode("Mac"))
	laptop.add_child(TreeNode("Surface"))
	laptop.add_child(TreeNode("Thinkpad"))

	cellphone = TreeNode("Cellphone")
	cellphone.add_child(TreeNode("iPhone"))
	cellphone.add_child(TreeNode("Vivo"))
	cellphone.add_child(TreeNode("Samsung Galaxy"))

	tv = TreeNode("TV")
	tv.add_child(TreeNode("Samsung"))
	tv.add_child(TreeNode("LG"))
	tv.add_child(TreeNode("Sony"))


	root.add_child(laptop)
	root.add_child(cellphone)
	root.add_child(tv)

	return root



if __name__ == '__main__':
	build_tree()