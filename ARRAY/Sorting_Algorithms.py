#sorting  algorithms

#SELECTION SORT
def selection_sort(arr):
	n = len(arr)
	for i in range(0, n):
		for j in range(i, n):
			if arr[j] < arr[i]:
				arr[i], arr[j] = arr[j], arr[i]
	return arr

#INSERTION SORT
def insertion_sort(arr):
	n = len(arr)
	for i in range(1, n):
		key = arr[i]
		j = i
		while j > 0  and arr[j-1] > key:
			arr[j] = arr[j-1]
			j-=1
		arr[j] = key
	return arr
	
#BUBBLE SORT
def bubble_sort(arr):
	n = len(arr)
	for i in range(0, n):
		for j in range(0, n-1):
			if arr[j] > arr[j+1]:
				arr[j+1], arr[j] = arr[j], arr[j+1]
	return arr

#QUICK SORT
def quick_sort(arr):
	pass


#to check once
#MERGE SORT
def merge(a, b):
	m = len(a)
	n = len(b)
	k = 0
	while i<m and j<n:
		if a[i] > b[j]:
			c[k] = b[j]
			j+=1
			k+=1

		elif a[i] < b[j]:
			c[k] = a[i]
			i+=1
			k+=1

		else:
			c[k] = b[j]
			k+=1
			j+=1
			c[k] = a[i]
			i+=1
			k+=1


	while j<n:
		c[k]= b[j]
		j+=1
		k+=1

	while i<m:
		c[k]= a[i]
		i+=1
		k+=1

	return c



def merge_sort(arr):
	mid = len(arr)/2
	l = arr[:mid]
	r = arr[mid+1:]

	left = merge_sort(l)
	right = merge_sort(r)
	return merge(l, r)


if __name__=="__main__":
	arr = [3,4, 8, 5, 7, 6, 2, 1]
	print "Initial Array: ", arr
	print "Bubble Sort: ", bubble_sort(arr)
	print "Insertion Sort: ", insertion_sort(arr)
	print "Selection Sort: ", selection_sort(arr)
	print "Quick Sort: ", quick_sort(arr)
	print "Merge Sort: ", merge_sort(arr)