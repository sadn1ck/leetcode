"""
Given a list of integers prices representing the stock prices of a company in chronological order, return the maximum profit you could have made from buying and selling that stock once.

You must buy before you can sell it.

Note: You are not required to buy or sell the stock.


"""

import math


class Solution:
    def solve(self, prices):
        mnprice = math.inf
        maxprofit = 0
        for price in prices:
            mnprice = min(mnprice, price)
            maxprofit = max(maxprofit, price-mnprice)
        return maxprofit
