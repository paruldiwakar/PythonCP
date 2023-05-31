class Solution:
    
    def maxSubarraySum(self, a, n):
        maxSum = a[0]
        currentSum = a[0]
        for i in range(1,n):
            currentSum = max(a[i], currentSum+a[i])
            if maxSum < currentSum:
                maxSum  = currentSum   
                     
        return maxSum
    
arr = [-1,-2,-3,-4,-5]    
sol = Solution() 
ans = sol.maxSubarraySum(arr, len(arr))    
print(ans)