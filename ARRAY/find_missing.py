from Sorting_Algorithms import selection_sort

def find_missing(arr):
    arr = selection_sort(arr)
    n = len(arr)
    for i in xrange(0, n):
        if i == 0 and arr[i] != 1:
            return 1
        if arr[i] != arr[i-1] + 1 and i != 0:
            return arr[i-1] + 1

#simplest one
def find_missing1(arr):
    n = len(arr)
    sum_n = ((n+1)*(n+2))/2
    sum_m = sum(arr)
    return sum_n - sum_m

print "Missing number is", find_missing1([1,2,3,4,6])