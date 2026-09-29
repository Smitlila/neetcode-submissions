class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                total = prices[j] - prices[i]
                p = max(total, p)
        
        return p