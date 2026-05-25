class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        if not prices:
            return 0
        else:
            while r <= len(prices)-1:
                if prices[r] - prices[l] > 0:
                    if prices[r] - prices[l] > profit:
                        profit = prices[r] - prices[l]
                    r += 1
                else:
                    if prices[r] < prices[l]:
                            l = r
                    r += 1
            return profit
        