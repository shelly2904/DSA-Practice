#Water Trap problem. How much water can be stored between the bars.

import numpy as np

def water_trap(arr):
	n = len(arr)
	left = np.array([0 for _ in range(0, n)])
	right = np.array([0 for _ in range(0, n)])

	left[0] = arr[0]
	right[n-1] = arr[n-1]

	for i in range(1, n):
		left[i] = max(left[i-1], arr[i])

	for i in range(n-2, -1, -1):
		right[i] = max(right[i+1], arr[i])


	water = 0
	for i in range(0,n):
		water += min(left[i], right[i]) - arr[i]

	print "total water require is ", water



if __name__=="__main__":
	A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
	water_trap(A)