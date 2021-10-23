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
# O(LOG N)
def partition(list, start, end):
    pivot = list[end]  # Partition around the last value
    bottom = start - 1  # Start outside the area to be partitioned
    top = end  # Ditto

    done = 0
    while not done:  # Until all elements are partitioned...

        while not done:  # Until we find an out of place element...
            bottom = bottom + 1  # ... move the bottom up.

            if bottom == top:  # If we hit the top...
                done = 1  # ... we are done.
                break

            if list[bottom] > pivot:  # Is the bottom out of place?
                list[top] = list[bottom]  # Then put it at the top...
                break  # ... and start searching from the top.

        while not done:  # Until we find an out of place element...
            top = top - 1  # ... move the top down.

            if top == bottom:  # If we hit the bottom...
                done = 1  # ... we are done.
                break

            if list[top] < pivot:  # Is the top out of place?
                list[bottom] = list[top]  # Then put it at the bottom...
                break  # ...and start searching from the bottom.

    list[top] = pivot  # Put the pivot in its place.
    return top  # Return the split point


def quicksort(list, start, end):
    if start < end:  # If there are two or more elements...
        split = partition(list, start, end)  # ... partition the sublist...
        quicksort(list, start, split - 1)  # ... and sort both halves.
        quicksort(list, split + 1, end)

    else:
        return
    return list


# to check once
# MERGE SORT
# O(N LOG N)
def merge_sort(arr):
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
        elif l[i] > r[j]:
            arr[k] = r[j]
            j += 1
        else:
            arr[k] = l[i]
            arr[k] = r[j]
            k += 1
            i += 1
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
        if i > max_ele:
            max_ele = i
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


if __name__ == "__main__":
    arr = [3, 4, 8, 5, 7, 6, 2, 1]
    # print "Initial Array: ", arr
    # print "Bubble Sort: ", bubble_sort(arr)
    # print "Insertion Sort: ", insertion_sort(arr)
    # print("Selection Sort: ", selection_sort(arr))
    # print "Quick Sort: ", quicksort(arr,0, len(arr)-1)
    print("Merge Sort: ", merge_sort(arr))
    # print "Bucket Sort", bucket_sort(arr)
