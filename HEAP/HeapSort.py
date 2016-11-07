import math

class Heap(object):
	def __init__(self):
		self.arr = []
		self.count = 0

	def insert_in_heap(self, value):
		#insert value at the end
		self.arr.insert(self.count, value)
		self.count += 1
		print self.arr
		self.heapify()
		print self.arr

	def heapify(self):
		i = self.count - 1
		print self.count
		while i>0 and self.arr[i] < self.arr[int(math.ceil((i-1)//2))]:
			print i , int(math.ceil((i-1)//2))
			self.arr[i], self.arr[int(math.ceil((i-1)//2))] = self.arr[int(math.ceil((i-1)//2))], self.arr[i]
			i = int(math.ceil((i-1)//2))


	def delete_from_heap(self, value):
		idx = self.arr.index(value)
		if not idx:
			return False

		self.count -= 1
		print self.arr[self.count]
		self.arr[idx] = self.arr[self.count]
		right = idx+1
		left = 0
		while left < self.count and (self.arr[idx] > self.arr[left] or self.arr[idx] > self.arr[right]):
			if self.arr[left] < self.arr[right]:
				self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
				left = idx
			else:
				self.arr[right], self.arr[idx] = self.arr[idx], self.arr[right]
				right = idx

		del self.arr[-1]


		


if __name__=="__main__":
	hp = Heap()
	arr = [2, 4, 6, 7, 8, 9, 5]
	for i in arr:
		hp.insert_in_heap(i)
	print hp.arr
	hp.delete_from_heap(4)
	print hp.arr

