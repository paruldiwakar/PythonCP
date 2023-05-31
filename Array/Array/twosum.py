class Solution:

    def binarySearch(self,arr, n, k):
        l = 0
        r = n-1
        m = (l+r)//2
        while l <= r:
            if arr[m] == k:
                return m
            elif arr[m] > k:
                r = m + 1
            else :
                l = m - 1
        return -1                

    def twoSum(self, nums, target) :
        nums.sort()
        n = len(nums)
        for i in range(n):
            x = target - nums[i]
            y = self.binarySearch(nums, n, x)
            if y>-1:
                return [i, y]
nums = [2,7,11,15]
target = 9  
s = Solution()
print(s.twoSum(nums, target))
          
            