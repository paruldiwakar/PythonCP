import numpy as np 
import time

class Solution:
    
    def segregateElements(self, arr):
        n = len(arr)
        temp1 = []
        temp2 = []
        for i in range(n):
            if arr[i] < 0:
                temp1.append(arr[i])
            else:
                temp2.append(arr[i])    
    
        arr = temp2 + temp1     
        return arr    
    
arr = input().split(' ')
arr = np.array(arr, dtype=int)
sol = Solution()
ans = sol.segregateElements(arr)
print(ans)