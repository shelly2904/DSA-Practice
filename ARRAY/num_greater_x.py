def bubble_sort(arr, idx):
	n = len(arr)
	for i in range(idx+1, n):
		for j in range(idx+1, n-1):
			if arr[j] > arr[j+1]:
				great = arr[j+1]
				small = arr[j]
				arr = arr[:j+1] + small + arr[j+1 + 1:]
				arr = arr[:j] + great + arr[j + 1:]
	return arr


def find_next_great(num):
	for i in range(len(num)-1, 0, -1):
		idx = i
		flag  = False
		while idx >= 0:
			idx -= 1
			if num[i] > num[idx]:
				great = num[idx]
				small = num[i]
				num = num[:idx] + small + num[idx + 1:]
				num = num[:i] + great + num[i + 1:]
				flag = True
				break
			else:
				pass
			
		if flag:
			break
		else:
			return num

	return bubble_sort(num, idx)
	
	





if __name__ == '__main__':
	print find_next_great('321')