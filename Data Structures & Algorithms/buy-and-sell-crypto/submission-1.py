class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        l, r = 0, 1
        res = prices[r] - prices[l]
        while r < len(prices):
            p = prices[r] - prices[l]
            res = max(res, p)
            if p < 0:
                l = r
                r += 1
            else:
                r += 1

        return max(res, 0)
            