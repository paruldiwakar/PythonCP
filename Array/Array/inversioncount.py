import numpy as np
class Solution:
    def __init__(self):
        self.c = 0
    
    def merge(self,arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)

        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
            
        i = 0	 # Initial index of first subarray
        j = 0	 # Initial index of second subarray
        k = l	 # Initial index of merged subarray
            
        
        while i < n1 and j < n2:
            if L[i] <= R[j]:
               arr[k] = L[i]
               i += 1
                
            else:
                arr[k] = R[j]
                j += 1
                self.c += m - i + 1
            k += 1
            
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1 
            
    def mergeSort(self, arr, l, r):
        if l < r:
            m = l+(r-l)//2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m+1, r)
            self.merge(arr, l, m, r) 
        return self.c           
    
    def inversionCount(self, a, n):
        return self.mergeSort(a, 0, n-1)
          
arr = [8, 4, 2, 1]  
'''     
468 335 1 170 225 479 359 463 465 206 146 282 328 462 492 496 443 328 437 392 105 403 154 293 383 422 217 219 396 448 227 272 39 370 413 168 300 36 395 204 312 323
''' 
#arr = input().split(' ')
#arr = np.array(arr, dtype=int)
n = len(arr)    
sol = Solution()
print(sol.inversionCount(arr, n))
