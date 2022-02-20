# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c = 1,0,0
        for _ in range(n):
            a,b,c = b,c,a+b+c
        return c
