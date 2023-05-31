class Solution:
    def doUnion(self, a, n, b, m):
        a,b = set(a), set(b)
        return len(a.union(b))
    
    def doIntersection(self, a, n, b, m):
        a,b = set(a), set(b)
        return len(a.intersection(b))    
'''
arr1 = input().split(' ')  
arr1 = np.array(arr1, dtype=int)
arr2 = input().split(' ') 
arr2 = np.array(arr2, dtype=int)
'''
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3]
sol = Solution() 
ans1 = sol.doUnion(arr1, len(arr1), arr2, len(arr2))   
ans2 = sol.doIntersection(arr1, len(arr1), arr2, len(arr2))
print(ans1, ans2)