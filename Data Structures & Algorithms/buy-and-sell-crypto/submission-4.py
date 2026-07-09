class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum_prices = [0]*(len(prices))

        for day_index in range(len(prices)):
            max_profit = 0
            for later_days in range(day_index, len(prices)):
                if(prices[later_days] > prices[day_index]):
                    potential_profit = prices[later_days]-prices[day_index]
                    if(potential_profit > max_profit):
                        max_profit = potential_profit
            maximum_prices[day_index] = max_profit
        return max(maximum_prices)
                
