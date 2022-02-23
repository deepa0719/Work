# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        
        MIN = -2147483648
        MAX = 2147483647
        
        a = 0
        if x<0:
            n = x*(-1)
        else:
            n = x
        while n!= 0:
            a = (a*10) + n%10
            n = n//10
            
        if x<0:
            a = a*(-1)
        return 0 if a>MAX or a<MIN else a
