class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)
        l_arr = [0] * n
        r_arr = [0] * n
        l_arr[0], l_arr[1] = arr[0],arr[0]
        r_arr[n-1], r_arr[n-2] = arr[n-1], arr[n-1]
        
        for i in range(2, n):
            l_arr[i] = arr[i-1] * l_arr[i-1]
            
        for i in range(n-3, -1, -1):
            r_arr[i] = arr[i+1] * r_arr[i+1]
        
        arr[0], arr[n-1] = r_arr[0], l_arr[n-1]
        
        for i in range(1, n-1):
            arr[i] = l_arr[i] * r_arr[i]
            
        return arr    
arr = [-1, 2, 3, 4]  
print(arr)      
sol = Solution()             
print(sol.productExceptSelf(arr)     )      