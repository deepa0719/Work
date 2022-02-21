#Given a roman numeral, convert it to an integer.
class Solution:
    def romanToInt(self, s: str) -> int:
        val = 0
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                val -= roman[s[i]]
            else:
                val += roman[s[i]]
        
        return val+roman[s[-1]]
