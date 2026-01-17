class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window, start with day1 and 2
        # curr = current day, nextd = next day
        curr = 0
        nextd = 1
        max_profit = 0


        while nextd < len(prices):
            # if current day is smaller then next, stay on day
            # if current day is larger than next, move to day
            # if next day is larger than current, move next and keep max
            # if next day is smaller than current, make that day current
            if prices[curr] < prices[nextd]:
                profit = prices[nextd] - prices[curr]
                max_profit = max(profit, max_profit)
            else: # curr > next day
                curr = nextd
            # move day 
            nextd += 1
        
            
        return max_profit