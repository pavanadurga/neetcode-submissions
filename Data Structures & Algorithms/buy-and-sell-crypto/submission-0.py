class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        cost=float("INF")
        for i in prices:
            cost=min(i,cost)
            profit=max(i-cost,profit)
        return profit