
def check_strict_increase(arr):

    i = 0
    j = len(arr) - 1
    ret = False
    while arr[i] <= arr[i+1]:
        i += 1

    ret = True

    j = len(arr) - 2
    while j >= i:
        if arr[j] <= arr[j+1]:
            j -= 1
        else:
            ret = False
            break
    return ret

print(check_strict_increase([1,2,10,5,7]))

