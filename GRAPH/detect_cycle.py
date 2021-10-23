from graph_traversals import Stack, dfs

def detect_cycle_directed(G, s):
	is_cyclic = False
	current = s

	RecurStack = Stack()
	NorStack = Stack()

	NorStack.push(current)
	while len(NorStack.arr) > 0:
		current = NorStack.pop()
		print("Traversing ", current)
		child = G[current]
		if any([True if c in RecurStack.arr else False for c in child ]):
			is_cyclic = True
		for i in child:
			NorStack.push(i)
		RecurStack.push(current)
	return is_cyclic


if __name__=="__main__":
	'''
	graph = {'0': set(['1', '2']),
		 '1': set(['2']),
		 '2': set(['0', '3']),
		 '3': set(['3'])}
	'''

	graph = {'0': set(['1']),
		 '1': set(['2']),
		 '2': set(['3']),
		 '3': []}

	start = '0'
	if detect_cycle_directed(graph, start):
		print("There is a cycle")
	else:
		print("There is no cycle")