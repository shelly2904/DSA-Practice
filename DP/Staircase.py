#find the number of ways we can reach nth stair

def climb_stair(n):
	if n == 0 or n == 1:
		return n
	return climb_stair(n-1) + climb_stair(n-2)


def find_staircase_dp(n):
	A =[]
	#insert base case
	A.insert(0,1)
	A.insert(1,1)
	A.insert(2,2) 
	A.insert(3,4)
	for i in range(4,n+1):
		val = A[i-1] + A[i-2] +A[i-3]
		A.insert(i,val)
	return A[n]


n = 8
print "the ways to reach ", n, " ", climb_stair(n)
print "the ways to reach ", n, " ", find_staircase_dp(n)