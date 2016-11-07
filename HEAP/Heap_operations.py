class Heap(object):
	def __init__(self):
		self.heap = []
		self.count = 0

	def insert(self, data, min=True):
		self.heap.insert(self.count, data)
		self.count += 1
		if min:
			self.heapify_min()
		else:
			self.heapify_max()


	def heapify_min(self):
		i = self.count - 1
		while i > 0 and self.heap[i] < self.heap[(i-1)/2]:
			self.heap[i], self.heap[(i-1)/2] = self.heap[(i-1)/2],  self.heap[i]
			i = (i-1)/2


	def heapify_max(self):
		i = self.count - 1
		while i > 0 and self.heap[i] > self.heap[(i-1)/2]:
			self.heap[i], self.heap[(i-1)/2] = self.heap[(i-1)/2],  self.heap[i]
			i = (i-1)/2


	def print_heap(self):
		print self.heap




if __name__=="__main__":
	print "Min Heap"
	minheap = Heap()
	minheap.insert(5)
	minheap.insert(1)
	minheap.insert(3)
	minheap.insert(4)
	minheap.insert(6)
	minheap.insert(9)
	minheap.print_heap()
	print

	print "Max Heap"
	maxheap = Heap()
	maxheap.insert(5, False)
	maxheap.insert(1, False)
	maxheap.insert(3, False)
	maxheap.insert(4, False)
	maxheap.insert(6, False)
	maxheap.insert(9, False)
	maxheap.print_heap()
