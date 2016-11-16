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
		return self.heap


	def delete(self, data, min=True):
		idx = self.heap.index(data)
		self.heap[idx], self.heap[self.count-1] = self.heap[self.count-1], self.heap[idx]
		del self.heap[self.count-1]
		self.count -= 1
		if min:
			self.heapify_min()
		else:
			self.heapify_max()


	def extract(self, min=True):
		ele = self.heap[0]
		if min:
			self.delete(self.heap[0])
		else:
			self.delete(self.heap[0], False)
		return ele




if __name__=="__main__":
	'''
	#Building a min heap
	print "Min Heap"
	minheap = Heap()
	minheap.insert(5)
	minheap.insert(1)
	minheap.insert(3)
	minheap.insert(4)
	minheap.insert(6)
	minheap.insert(9)
	#print minheap.print_heap()
	minheap.delete(3)
	#print minheap.print_heap()
	print

	#Building a max heap
	print "Max Heap"
	maxheap = Heap()
	maxheap.insert(5, False)
	maxheap.insert(1, False)
	maxheap.insert(3, False)
	maxheap.insert(4, False)
	maxheap.insert(6, False)
	maxheap.insert(9, False)
	#print maxheap.print_heap()
	'''

	#find k-largest element
	'''
	k = 2
	arr = [1,2,5,6,3]
	maxheap = Heap()
	for i in arr:
		maxheap.insert(i, False)
	arr = maxheap.print_heap()
	for i in range(0, k):
		maxheap.extract(False)
	'''

	k = 3
	arr = [1,2,5,6,3]
	minheap = Heap()
	for i in arr:
		minheap.insert(i)
	arr = minheap.print_heap()
	for i in range(0, k):
		print minheap.extract()

	

	'''
	#Merge K-sorted arrays:
	arrays = [[2,4,5], [1,3,8]]
	n = len(arrays[0])
	k = len(arrays)
	minheap = Heap()
	new_arr = []
	i = 0
	while i< n:
		arr_temp = [a[i] for a in arrays]
		for ele in arr_temp:
			minheap.insert(ele)
		i+=1

	#print minheap.heap
	while minheap.heap:
		mini = minheap.extract()
		new_arr.append(mini)
		#print minheap.heap
	#print new_arr

	'''





