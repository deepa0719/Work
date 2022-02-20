# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums)//2
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t+nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False
