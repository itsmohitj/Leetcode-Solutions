"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell_val = 0
        purchase_val = float('inf')
        profit = 0
        for i in prices:
            if i < purchase_val:
                purchase_val = i
            sell_val = i
            if sell_val - purchase_val > profit:
                profit = sell_val-purchase_val
        return profit

# Time Complexity = O(n)
# Space Complexity = O(1)
