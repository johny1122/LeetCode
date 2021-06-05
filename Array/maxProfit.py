# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like
# (i.e., buy one and sell one share of the stock multiple times).

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0

        profit = 0
        buy = True
        value_owned = 0

        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:  # price go up
                if buy:
                    buy = False
                    value_owned += prices[i]
                continue

            if prices[i] > prices[i + 1]:  # price go down
                if not buy:  # need to sell
                    buy = True
                    profit += prices[i] - value_owned
                    value_owned = 0

        if not buy:  # need to sell on last day
            profit += prices[-1] - value_owned
        return profit


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))   # should return 7
    print(solution.maxProfit([1, 2, 3, 4, 5]))      # should return 4
    print(solution.maxProfit([7, 6, 4, 3, 1]))      # should return 0
    print(solution.maxProfit([2, 1, 2, 0, 1]))      # should return 2
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))   # should return 7
