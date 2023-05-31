'''
Merge 2 sorted arrays 
Input: 
n = 4, arr1[] = [1 3 5 7] 
m = 5, arr2[] = [0 2 6 8 9]
Output: 
arr1[] = [0 1 2 3]
arr2[] = [5 6 7 8 9]
'''
class Solution:
    def merge(self, a, b, n, m):
        i = n-1
        j = 0
        while i >= 0 and j < m:
            if a[i] > b[j]:
                t = a[i]
                a[i] = b[j]
                b[j] = t
                i -= 1
            else:
                j+=1    
        a.sort(), b.sort()       
        return a,b

    
n = 4
arr1 = [1, 3, 5, 7] 
m = 5
arr2 = [0, 2, 6, 8, 9]
sol = Solution()    
ans = sol.merge(arr1, arr2, n, m)
print(ans)