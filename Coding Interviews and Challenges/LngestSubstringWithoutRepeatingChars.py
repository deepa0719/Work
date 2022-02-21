#Given a string s, find the length of the longest substring without repeating characters.


#Using Sliding Window, we first declare a set in which we store the occurence of the characters as we traverse the string. If we encounter a duplicate, we pop the left most char in the set and we keep popping it till the string is valid again.
#i.e. does not contain any duplicate. So, we need to keep incrementing the left pointer. After this, we add the next char to the set and check if the length of the substring is maximum or not.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
        return res
