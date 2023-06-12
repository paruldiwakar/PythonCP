class Solution:

    def repeatedNumber(self, A):
        n = len(A)
        output = [0] * n
        for i in range(n):
            output[A[i]-1] += 1
        o = len(output)
        for i in range(n):
            if output[i] > 1:
                output.append(i+1)  
        for i in range(n):
            if output[i] == 0:
                output.append(i+1)          
        output = output[o:]        
        return output
arr = [1, 1, 2, 3, 4]
sol = Solution()
ans = sol.repeatedNumber(arr)
print(ans)