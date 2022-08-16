'''
---Description---
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
----Source---

'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        pre_min = prices[0] if prices else 0
        for price in prices:
          profit = max(profit, price - pre_min)
          pre_min = min(pre_min, price)

        return profit

## test code
test_prices = [3,8,1,6]
test = Solution
outPut = test.maxProfit(test,test_prices)
print("Output: ", outPut)  