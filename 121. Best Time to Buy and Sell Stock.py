
'''https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1206578919/'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0 
        l, r= 0 , 1
        while  r < len(prices):           
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                prof = max(prof,profit)

            else:
                l=r
            r+=1
            
        return prof
                
        