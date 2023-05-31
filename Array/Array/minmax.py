import numpy as np 

def minmax(arr):
    min = arr[0]
    max = arr[0]
    
    for i, a in enumerate(arr):
        if a > max:
            max = a
        if a < min:
            min = a
            
    return max, min            


arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))
    
arr = np.array(arr)
print(minmax(arr)[0], minmax(arr)[1])
   