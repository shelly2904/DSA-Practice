#Edit Distance Problem

import numpy as np

def edit_distance(X, Y):
	n = len(X)
	m = len(Y)

	T = [[0 for _ in range(0, m)] for _ in range(0, n)]
	T = np.array(T)

	for i in range(0, n):
		for j in range(0, m):
			if X[i] == Y[j]:
				T[i][j] = T[i-1][j-1]

			else:
				T[i][j] = min(T[i-1][j], T[i][j-1]) + 1
	
	return T[-1][-1]


print edit_distance('MADAM', 'MADAM')
