"""https://leetcode.com/problems/group-anagrams/"""

import random
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictio={}

        for i in strs:
            key = tuple(sorted(i))
    
            if key in dictio:
                dictio[key].append(i)
            else:
                dictio[key] = [i]
        return list(dictio.values())
    
        
s= Solution()        
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))