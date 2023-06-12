'''
Array is sorted but rotated by a pivot
12345 -> 45123
'''
class Solution:
    def search(self, arr, target):
        l, r = 0, len(arr) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return mid
            
            if arr[l] <= arr[mid]: #left sorted subarray
                if target < arr[l] or target > arr[mid]:
                    l = mid +1
                else:
                    r = mid - 1    
            else: #right sorted array
                if target > arr[r] or target < arr[mid]:
                    r = mid - 1
                else:
                    l = mid + 1    
        return -1                      
                
    def findMin(self, arr):
        l, r, minimum = 0, len(arr) - 1, arr[0]
        
        while l <= r:
            if arr[l] < arr[r]:
                minimum = min(minimum, arr[l])
                break
            
            mid = (l + r) // 2
            minimum = min(minimum, arr[mid])
            if arr[mid] >= arr[l]: #mid is part of left subarray
                l = mid + 1
            else:
                r = mid - 1                    
        return minimum
arr = [4, 5, 6, 7, 11, 2]   
target = 10
sol = Solution()
#ans1 = sol.search(arr, target)
#print(ans1)    
ans2 = sol.findMin(arr)
print(ans2)
    