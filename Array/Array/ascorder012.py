class Solution:
    def sortColors(self, arr) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        n = len(arr)
        count = [0, 0, 0]
        for i in range(n):
            count[arr[i]] += 1
        for i in range(1,len(count)):
            count[i] += count[i-1] 
        
        n1, n2 = count[0], count[2]
        i, j = 0, count[1]
        
        while i < n1 or j < n2:
            if i < n1 and j < n2:
                arr[i] = 0
                arr[j] = 2
                i += 1
                j += 1
            elif i < n1 and j >= n2:
                arr[i] = 0
                i += 1
            elif i >= n1 and j < n2:
                arr[j] = 2
                j += 1
                    
        for i in range(n1, count[1]):
            arr[i] = 1        
arr = [0, 0, 0, 0, 0, 0, 2, 1, 1, 2, 1, 1, 1, 1, 2]
sol = Solution()
sol.sortColors(arr)
print(arr)