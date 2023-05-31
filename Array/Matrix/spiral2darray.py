class Solution:
    def printspiral(self, arr):
        rows = len(arr)
        cols = len(arr[0])
        total_elements = rows*cols
        spiral = [0] * total_elements 
        c = 0
        left, right = 0, cols - 1
        top, bottom = 0, rows - 1
        while left <= right and top <= bottom and c < total_elements:
            for i in range(left, right+1):
                if  c < total_elements:
                    spiral[c] = arr[top][i]
                    c += 1
            top += 1
            
            for i in range(top, bottom+1):
                if  c < total_elements:
                    spiral[c] = arr[i][right]
                    c += 1
            right -= 1
            
            for i in range(right, left-1, -1):
                if  c < total_elements:
                    spiral[c] = arr[bottom][i]
                    c += 1
            bottom -= 1
            
            for i in range(bottom, top-1, -1):
                if  c < total_elements:
                    spiral[c] = arr[i][left]
                    c += 1
            left += 1    
            
        return spiral

arr1 = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]  
arr2 = [[1,2,3,4,5],
       [6,7,8,9,10],
       [11,12,13,14,15],
       [16,17,18,19,20],
       [21,22,23,24,25]]
arr3 = [[6, 6, 2],
        [28, 2, 7],
        [23, 4, 3],
        [25, 22, 12],
        [26, 3, 28]]
arr = arr3
row = len(arr)
col = len(arr[0])
print('Input Array')
for i in range(row):
       for j in range(col):
              print(arr[i][j], end=' ')
       print()     
sol = Solution()          
print('Spiraled Array')
print(sol.printspiral(arr))
