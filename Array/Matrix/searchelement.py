class Solution:
    def binarysearch(self, arr, up_row, down_row, key):
        if up_row <= down_row:
            mid_row = up_row + (down_row - up_row)//2
            l, r = 0, len(arr[0])-1
            #print('l and r and mid_row', l, r, mid_row)
            if arr[mid_row][l] <= key and arr[mid_row][r] >= key: 
                while l <= r:
                    mid = l + (r - l) // 2
                    if arr[mid_row][mid] == key:
                        return True
                    elif arr[mid_row][mid] > key:
                        r = mid - 1
                    elif arr[mid_row][mid] < key:
                        l = mid + 1     
                return False  
                    
            elif arr[mid_row][l] > key:
                down_row = mid_row - 1
                return self.binarysearch(arr, up_row, down_row, key)

            elif arr[mid_row][r] < key:
                up_row = mid_row + 1
                return self.binarysearch(arr, up_row, down_row, key)
        else:
            return False
        
    def binarysearch2(self, arr, up_row, down_row, key):
        while up_row <= down_row:
            mid_row = up_row + (down_row - up_row)//2
            l, r = 0, len(arr[0])-1
            if arr[mid_row][l] <= key and arr[mid_row][r] >= key: 
                while l <= r:
                    mid = l + (r - l) // 2
                    if arr[mid_row][mid] == key:
                        return True
                    elif arr[mid_row][mid] > key:
                        r = mid - 1
                    elif arr[mid_row][mid] < key:
                        l = mid + 1     
                return False  
            
            elif arr[mid_row][l] > key:
                down_row = mid_row - 1
                
            elif arr[mid_row][r] < key:
                up_row = mid_row + 1    
        return False
    
    def searchMatrix(self, matrix, target):
        up = 0
        down = len(matrix) 
        
        ans = self.binarysearch2(matrix, up, down-1, target)
        return ans
    
    
    
    
sol = Solution()
matrix = [[1,3,5,7], [10,11,16,20], [23,30,34,60]]

'''
matrix = [[1,1]]
key = 2
ans = sol.searchMatrix(matrix, key)
print(f'{key} present in Matrix? {ans}')
'''
for i in range(3):
    for j in range(4):
        key = matrix[i][j]
        ans = sol.searchMatrix(matrix, key)
        print(f'{key} present in Matrix? {ans}')
