class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Method 1
        # nums1.extend(nums2)
        # nums1.sort()
        # if len(nums1)%2!=0:
        #     return nums1[len(nums1)//2]
        # else:
        #     return (nums1[len(nums1)//2 -1]+ nums1[len(nums1)//2])/2
        
        #Method 2
        m = len(nums1)
        n = len(nums2)
        total = m + n
        half = total//2
        
        if len(nums2) < len(nums1):
            nums1, nums2 =nums2, nums1
        
        l, r = 0, len(nums1) - 1
        while True:
            i = (l+r)//2 # middle of nums1
            j = half - i - 2 # nums2
            
            Left1 = nums1[i] if i >= 0 else float("-infinity")
            Right1 = nums1[i+1] if i+1 < len(nums1) else float("infinity")
            Left2 = nums2[j] if j >= 0 else float("-infinity")
            Right2 = nums2[j + 1] if j+1 < len(nums2) else float("infinity")
            
            #partition is correct
            if Left1 <= Right2 and Left2 <= Right1:
                if total%2:
                    return min(Right1, Right2)
                return (max(Left1, Left2) + min(Right1, Right2))/2
            elif Left1 > Right2:
                r = i-1
            else:
                l = i+1
