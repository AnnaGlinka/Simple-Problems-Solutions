from typing import List
"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
https://www.airbnb.com/rooms/37586126?check_in=2021-06-01&source_impression_id=p3_1680006346_TfU%2FgCa8Ex80FLUB&guests=1&adults=1#availability-calendar
O(N)
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        lowest_price = prices[0]
        for price in prices:
            if price < lowest_price:
                lowest_price = price

            elif price - lowest_price > max_prof:
                max_prof = price - lowest_price

        return max_prof
                
        
        
        



s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))