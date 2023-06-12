class Solution:
    def majorityElement(self, arr):
        freq = {}
        n = len(arr)
        for i in range(len(arr)):
            freq[arr[i]] = 0
        for i in range(len(arr)):
            freq[arr[i]] += 1
        for key, val in freq.items():
            if val > n//2:
                return key
        return
    
    def majorityElement2(self, arr):
        n = len(arr)
        count = 1
        maj_idx = 0
        for i in range(1, n):
            if arr[maj_idx] != arr[i]:
                count -= 1
            else:
                count += 1    
            if count == 0:
                maj_idx = i
                count += 1   
        print(maj_idx)
        if arr.count(arr[maj_idx]) > n//2:       
            return arr[maj_idx]     
        return    
    
    
nums = [6,5,6]
sol = Solution()
ans = sol.majorityElement2(nums)
print(ans) 