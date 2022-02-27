# Given an integer x, return true if x is palindrome integer. An integer is a palindrome when it reads the same backward as forward. 
# For example, 121 is a palindrome while 123 is not.
 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        a = 0
        n = x
        
        #Reverse the number
        while x!= 0:
            a = a*10 + x%10
            x = x//10
        
        #Compare original and reversed numbers
        if a!=n:
            return False
        return True
