def rotate( arr, n):
    s = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]

    arr[0] = s
    return arr

arr = [1, 2, 3, 4, 5]
print(rotate(arr, len(arr)))       