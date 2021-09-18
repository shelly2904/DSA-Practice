(n, k, q) = map(int, input().split(' '))
a = map(int, input().split(' '))

for _ in range(q):
	x = int(input())
	print(a[(x-k)%n])



'''
def GCD(a, b):
	rem= a%b
	while rem!=0:
		a = b
		b = rem
		rem = a%b
	return b

g = GCD(n, k)

for i in range(0, g):
	temp = a[i]
	j = i
	while True:
		m = j+k
		if m >= k:
			m = m-k
		if k == i:
			break
		a[j] = a[m]
		j = m
	a[j] =temp


try:
	while True:
		inp = raw_input()
		if not inp:
			break
		print a[int(inp)]
except:
	pass
'''



