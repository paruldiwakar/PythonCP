class Solution:
    def findPairs(self, arr, k): #using hashmap
        freq = {}
        for i in range(len(arr)):
            if arr[i] in freq.keys():
                freq[arr[i]] += 1
            else :    
                freq[arr[i]] = 1 
        count = 0        
        if k == 0:
            for key, val in freq.items():
                if val > 1:
                    count += 1
        else:
            for key,val in freq.items():
                if key+k in freq.keys():
                    count += 1
        return count                                    
nums = [3,1,4,1,5]
k = 2   
sol = Solution()
ans = sol.findPairs(nums, k)
print(ans)
