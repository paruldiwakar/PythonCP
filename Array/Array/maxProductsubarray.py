class Solution:
    def maxSubarrayProduct(self, arr):
        n = len(arr)
        l_arr = [0] * n
        r_arr = [0] * n
        l_arr[0] = arr[0]
        r_arr[n-1] = arr[n-1]
        
        for i in range(1, n):
            if l_arr[i-1]:
                l_arr[i] = l_arr[i-1] * arr[i]
            else:
                l_arr[i] = arr[i]
        for i in range(n-2, -1, -1):
            if r_arr[i+1]:
                r_arr[i] = r_arr[i+1] * arr[i]
            else:
                r_arr[i] = arr[i]
                
        maxProduct = max(l_arr[0], r_arr[0])
        for i in range(1,n):
            currentProduct = max(max(l_arr[i], r_arr[i]), arr[i])
            if maxProduct < currentProduct:
                maxProduct =  currentProduct
        return maxProduct        
    
arr1 = [-1,-2,-3,-4,-5] 
arr2 = [-2,11-2]
arr3 = [-1,-2,-3,0]
sol = Solution() 
ans = sol.maxSubarrayProduct(arr3)    
print(ans)