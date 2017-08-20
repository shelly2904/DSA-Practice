#Given an array where the array is sorted in ascending order then in descending order, 
#arrange this array in sorted manner aesc.

def find_split(arr):
	print arr
	breakpoint = 0
	for i in range(0, len(arr)):
		if arr[i] > arr[i+1]:
			breakpoint = i
			break
	return breakpoint

def sort_arr(arr, idx):
	n = len(arr)
	for i in range(idx, n):
		for j in range(idx, n-1):
			if arr[j] > arr[j+1]:
				arr[j+1], arr[j] = arr[j], arr[j+1]
	print arr



if __name__=="__main__":
	A = [1,2,3,4,5,6,10,9,8,7]
	breakpoint = find_split(A)
	print breakpoint
	sort_arr(A, breakpoint)
