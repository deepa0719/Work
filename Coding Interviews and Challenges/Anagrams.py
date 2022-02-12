#First Method (T(n) = O(nlogn), S(n)= O(n))
def anagram(a, b):
  if len(a)!=len(b):
    return False
  return sorted(a)==sorted(b)


#Second Method (T(n)=O(n), Space Complexity = O(n))
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
      
#Third Method
from collections import Counter
def anagram(input1, input2):
    return Counter(input1) == Counter(input2)
