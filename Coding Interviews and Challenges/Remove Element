class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for i in range(1, len(nums)+1):
            if nums[i-1] == val:
                cnt += 1
            else:
                nums[i-1-cnt] = nums[i-1]
        return len(nums) - cnt
