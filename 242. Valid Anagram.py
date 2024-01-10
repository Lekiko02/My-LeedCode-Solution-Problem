""" https://leetcode.com/problems/valid-anagram/"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
    
        
        sorted_s =sorted(s)
        sorted_t = sorted(t)
        
        for i in range(len(sorted_s)):
            if sorted_s[i]!=sorted_t[i]:
                return False
        return True
       
solution = Solution() 

s = "anagram" 
t = "nagaram"
s1 = "rat"
t1 = "car"
print(solution.isAnagram(s,t))
print(solution.isAnagram(s1,t1))