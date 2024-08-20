class Solution:
    def maxProfit(self, prices) -> int:
        """
        essentially find the greatest difference between two numbers in the list
        big number has to go first

        only need to check which days make the most profit, hence move p1 to p2

        make two pointers
        set pointer 1 to be 0 and p2 to be 1
        check if next value is bigger
        if bigger, check for profit
        compare with max profit
        else move p1 to p2
        increment p2
        """

        b, s = 0, 1
        max_profit = 0

        while s < len(prices):
            if prices[b] < prices[s]:
                profit = prices[s] - prices[b]
                max_profit = max(max_profit, profit)
            else:
                b = s
            s += 1

        return max_profit
