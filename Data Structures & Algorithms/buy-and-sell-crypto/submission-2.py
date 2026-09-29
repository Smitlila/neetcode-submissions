class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        mini = float("inf")

        for i in range(len(prices)):
            mini = min(mini, prices[i])
            maxi = max(maxi, prices[i] - mini)

        return maxi
        
        # p = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         total = prices[j] - prices[i]
        #         p = max(total, p)
        
        # return p