def find_ic(arr):
	ic = 0
	for i in range(0, len(arr)):
		for j in range(0, len(arr)):
			if arr[i] > arr[j] and i<j:
				ic += 1
	return ic


print find_ic([1,5,3,2,4])