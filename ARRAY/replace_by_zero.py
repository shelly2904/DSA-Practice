#Program to replace all elements to zero in row and column if a particular element is zero
import numpy as np
import copy

#Approach 1: take 2 arrays to store index 
#Approach 2: replace 0th element

def approach_1(A):
	row_idx = []
	col_idx = []
	rows, cols = A.shape
	for r in range(0, rows):
		for c in range(0, cols):
			if A[r][c] == 0:
				row_idx.append(r)
				col_idx.append(c)
	for i in row_idx:
		for j in range(0, cols):
			A[i][j] = 0
	for i in col_idx:
		for j in range(0, rows):
			A[j][i] = 0
	print A


def approach_2(A):
	rows, cols = A.shape
	for r in range(0, rows):
		for c in range(0, cols):
			if A[r][c] == 0:
				A[0][c] = 0
				A[r][0] = 0
	for i in range(0, cols):
		if A[0][i] == 0:
			for j in range(1, rows):
				A[j][i] = 0
			break
	for i in range(0, rows):
		if A[i][0] == 0:
			for j in range(1, cols):
				A[i][j] = 0
			break
	print A
	
		
if __name__ == '__main__':
	B = np.array([[1,2,3,4,4], [1,4,5,2,0], [1,2,3,4,5]])
	C = copy.deepcopy(B)
	print B
	approach_2(C)
