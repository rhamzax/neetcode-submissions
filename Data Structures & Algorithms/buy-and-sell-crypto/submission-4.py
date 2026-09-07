class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0
        while left != len(prices) - 1:
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
            if prices[left] > prices[right] and right != len(prices) - 1:
                left += 1
                right += 1
            elif right == len(prices) - 1:
                left += 1
            else:
                right += 1
        return maxProfit