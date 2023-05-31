class Solution:
    def findDuplicates(self, arr):
        n = len(arr) 
        output = [0] * n
        for i in range(n):
            output[arr[i-1]-1] += 1
        o = len(output)
        for i in range(n):
            if output[i] > 1:
                output.append(i+1)  
        output = output[o:]        
        return output        

arr = [4,3,2,7,8,2,3,1]
sol = Solution()
ans = sol.findDuplicates(arr)    
print(ans)