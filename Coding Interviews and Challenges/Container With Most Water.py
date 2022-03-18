# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #Start with a left pointer at the extreme left and a right pointer at the extreme right
        #Check the max area
        #Choose the minimum out of the two pointers and move the min value pointer to left/right accordingly
        
        l,r = 0, len(height)-1
        maxarea = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxarea = max(maxarea,area)
            
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
        return maxarea
