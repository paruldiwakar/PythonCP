def reversedArray(arr):
    l = 0
    r = len(arr) - 1
    i, j = l, r
    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

array = [3, 9, 1, 19, 0, 12]
reversedArray(array)
print(array)