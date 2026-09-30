class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        p = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                total = prices[r] - prices[l]
                p = max(p, total)
            else:
                l = r
            
            r += 1
        return p

        # maxi = 0
        # mini = float("inf")

        # for i in range(len(prices)):
        #     mini = min(mini, prices[i])
        #     maxi = max(maxi, prices[i] - mini)

        # return maxi
        
        # p = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         total = prices[j] - prices[i]
        #         p = max(total, p)
        
        # return p