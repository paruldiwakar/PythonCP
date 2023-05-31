class Solution:
    def trappingWater(self, arr,n):
        l_arr = [0]*n
        r_arr = [0]*n
        l_arr[0] = arr[0]
        r_arr[n-1] = arr[n-1]
        result = 0
        for i in range(1,n):
            l_arr[i] = max(l_arr[i-1],arr[i])
        print(l_arr)    
        for i in range(n-2,-1,-1):
            r_arr[i] = max(r_arr[i+1],arr[i])    
            print(r_arr[i])
        print(r_arr)     
        for i in range(n):
            result += min(l_arr[i],r_arr[i]) - arr[i]    
        
        return result    
    
sol = Solution()
arr = [7,4,0,9]
n = len(arr)
print(sol.trappingWater(arr, n)) 