class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        bmin = prices[0]
        bmax = 0
        
        for i in range(1, len(prices)):
            if prices[i] < bmin:
                bmin = prices[i]
            elif prices[i] - bmin > bmax:
                bmax = prices[i] - bmin
            else:
                pass
        return bmax