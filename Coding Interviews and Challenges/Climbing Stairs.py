#You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#Answer -> Make a decision tree and take the bottom up approach. We then see that there are many similar branches which we need not calculate each time. 
# If say, n = 6, and we take an array to showcase the number of ways we can reach the array would look like -> [13, 8, 5, 3, 2 , 1, 1]. So there are 13 ways of reaching the top of 6 stairs.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        one_step, two_step = 1, 1
        for i in range(n-1):
            a = one_step + two_step
            two_step = one_step
            one_step = a
        return a
