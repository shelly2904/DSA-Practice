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


def reverse(string):
	st = Stack()
	for i in range(0, len(string)):
		st.push(string[i])
	string = ''
	while st.arr:
		string += st.pop()
	print string

if __name__ == '__main__':
	A = 'shalini'
	reverse(A)