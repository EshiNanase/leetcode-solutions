class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profit = 0
        purchase = prices[0]
        
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - purchase)
            purchase = min(purchase, prices[i])
        return profit
        