#Given an array, find the pair which result in sum = x

def find_pair(arr, x):
	#sort the elements
	start = 0
	end = len(arr)-1
	while start < end:
		print start, end
		if (arr[start] + arr[end]) == x:
			return (start, end)
		elif  arr[start] + arr[end] > x:
			end -= 1
		else:
			start += 1
	return None

print find_pair([1,3,4,5,6], 4)





