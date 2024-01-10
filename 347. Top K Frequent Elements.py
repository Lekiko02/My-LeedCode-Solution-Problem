"""https://leetcode.com/problems/top-k-frequent-elements/"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    
        count = {}
        freq=[[] for i in range(len(nums) +1)]
        
        for key in nums:
            count[key]= 1 + count.get(key,0)
            
        for key, value in count.items():
            freq[value].append(key)
        res=[]
        for i in range(len(freq) -1 , 0, -1):
            for key in freq[i]:
                res.append(key)
                if len(res)==k:
                    return res
                
    

           

nums = [1,1,1,2,2,3]
k = 2                
s = Solution()     
print(s.topKFrequent(nums,k))