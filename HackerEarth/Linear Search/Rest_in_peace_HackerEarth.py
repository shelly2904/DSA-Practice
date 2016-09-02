import numpy as np

def LCS(X, Y):
	m = len(X)
	n = len(Y)
	Z = [[0 for _ in range(0, n+1)] for _ in range(0, m+1)]
	D = [["" for _ in range(0, n+1)] for _ in range(0, m+1)]
	Z=  np.array(Z)
	D=  np.array(D)
	for i in range(1, m+1):
		for j in range(1, n+1):
			if X[i-1] == Y[j-1]:

				Z[i][j] = Z[i-1][j-1] + 1
				D[i][j] = "d"
			else:
				Z[i][j] = max(Z[i-1][j], Z[i][j-1])
				if Z[i][j] == Z[i-1][j]:
					D[i][j] = "u"
				else:
					D[i][j] = "l"

	LCS_str = np.array(['' for _ in range(0, Z[-1][-1])])
	length = Z[-1][-1] - 1
	while i > 0  and j > 0:
		if D[i][j] == "l":
			j-=1
		elif D[i][j] == "u":
			i -= 1
		else:
			LCS_str[length] = Y[j-1]
			length -= 1
			i -= 1
			j -= 1

	res = ''.join(LCS_str)
	res.strip(' ')
	return res 



if __name__== "__main__":
	n = int(raw_input())
	input = []
	for i in range(0, n):
		input.append(raw_input())


	for i in input:
		if int(i) % 21 == 0:
			print "The streak is broken!"
		elif '21' in i:
			print "The streak is broken!"
		else:
			print "The streak lives still in our heart!"
			


