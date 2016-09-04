import numpy as np

		
def detect_coins(D, arr, X):
	(row, col) = np.shape(D)
	i = row-1
	j = col-1

	ans = []
	while i != 0 and j != 0:
		#import pdb; pdb.set_trace()
		if D[i][j] == "up":
			i -= 1
		if D[i][j] == "le":
			j -= arr[i]
			ans.append(arr[i])

	print ans
	

def coin_change(X, arr):
	T = [[x for x in range(0, X+1)] for _ in range(0, len(arr))]
	D = [["up" for x in range(0, X+1)] for _ in range(0, len(arr))]
	T = np.array(T)
	D = np.array(D)
	for i in range(1, len(arr)):
		for j in range(1, X+1):
			if i > j:
				T[i][j] = T[i-1][j]
				D[i][j] = "up"
			else:
				T[i][j] = min(T[i-1][j], T[i][j-arr[i]] + 1)
				if T[i][j] ==  T[i][j-arr[i]] + 1:
					D[i][j] = "le"

	detect_coins(D, arr, X)
	print "Total minimum number of coins", T[-1][-1]

coin_change(8, [1,5,6,8])
