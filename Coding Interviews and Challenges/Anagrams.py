#Method 1: Using sorted()  (T(n) = O(nlogn), S(n)= O(n))
def anagram(a, b):
  if len(a)!=len(b):
    return False
  return sorted(a)==sorted(b)


#Method 2: Using dictionaries (T(n)=O(n), Space Complexity = O(n))
def anagrams(s1, s2):
    if len(s1)!=len(s2):
        return False
    freq1 = {}
    freq2 = {}
    for i in s1:
        if i in freq1:
            freq1[i] += 1
        else:
            freq1[i]=1
    for i in s2:
        if i in freq2:
            freq2[i] += 1
        else:
            freq2[i]=1
    for key in freq1:
        if key not in freq2 or freq1[key]!=freq2[key]:
            return False
        return True
      
#Method 3: Using collections
from collections import Counter
def anagram(input1, input2):
    return Counter(input1) == Counter(input2)

  
#Method 4: Using dictionaries (more elegant approach)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countS, countT = {}, {}
        
        #iterate through s and t
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #get() method is used to check the previously occurring character in string, if its new, it assigns 0 as initial and appends 1 to it, else appends 1 to previously holded value of that element in dictionary.


            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
