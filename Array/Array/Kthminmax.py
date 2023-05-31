#solve using min heap

def kthminmax(arr, k):
    arr.sort
    return arr[k-1]

array = [3, 9, 1, 19, 0, 12]
K = 4
print(kthminmax(array, K))
