class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
                
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1    
        
        while j < len(nums2):   
            merged.append(nums2[j])
            j += 1
        print(merged)    
        if len(merged) % 2 == 1:
            return  merged[len(merged)//2]
        return (merged[len(merged)//2] + merged[len(merged)//2 -1])/2 
    
    def findMedianSortedArrays2(self, nums1, nums2):
        merged = []
        m = len(nums1) + len(nums2)
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2) and i+j <= m//2:   
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1            
        while i < len(nums1) and i+j <= m//2:
            merged.append(nums1[i])
            i += 1    
        while j < len(nums2) and i+j <= m//2:   
            merged.append(nums2[j])
            j += 1    
        print(merged)    
        if m % 2 == 1:
            return merged[-1] 
        return (merged[-1] + merged[-2])/2
    
arr1 = [-5, 3, 6, 12, 15]
arr2 = [-12, -10, -6, -3, 4, 10]
sol = Solution()
ans = sol.findMedianSortedArrays2(arr1, arr2)
print(ans)