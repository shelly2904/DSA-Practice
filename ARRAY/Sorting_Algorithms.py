# sorting  algorithms

# SELECTION SORT
# O(N^2)
def selection_sort(arr):
    n = len(arr)
    for i in range(0, n):
        min_idx = i
        for j in range(i, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# INSERTION SORT
# O(N^2)
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i
        while j > 0 and arr[j - 1] > key:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = key
    return arr


# BUBBLE SORT
# O(N^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr


# QUICK SORT
# O(N LOG N)
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

# to check once
# MERGE SORT
# O(N LOG N)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]

        merge_sort(l)
        merge_sort(r)
        m = len(l)
        n = len(r)
        i = j = k = 0

        while i < m and j < n:
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < m:
            arr[k] = l[i]
            i += 1
            k += 1

        while j < n:
            arr[k] = r[j]
            k += 1
            j += 1

    return arr


# BUCKET SORT
# O(N)
def find_max(arr):
    max_ele = 0
    for i in arr:
        max_ele = max(max_ele, i)
    return max_ele


def bucket_sort(arr):
    max_ele = find_max(arr)
    counter = [0] * (max_ele + 1)
    for i in arr:
        counter[i] += 1
    sorted_array = []
    for num, i in enumerate(counter):
        sorted_array.extend([num] * i)
    return sorted_array


# if __name__ == "__main__":
array = [3, 4, 8, 5, 7, 6, 2, 1]
# print "Initial Array: ", arr
# print "Bubble Sort: ", bubble_sort(arr)
# print "Insertion Sort: ", insertion_sort(arr)
# print("Selection Sort: ", selection_sort(arr))
# quick_sort(array,0, len(array)-1)
# print(array)
# print("Merge Sort: ", merge_sort(arr))
print("Bucket Sort", bucket_sort(array))
