#You are given an array prices where prices[i] is the price of a given stock on the i-th day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve.
#If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self,prices):
        i=0
        j=1
        profit=0
        while j<len(prices):
            if prices[j]-prices[i]>profit:
                profit=prices[j]-prices[i]
            else:
                if prices[j] < prices[i]:
                    i=j
            j=j+1
        return profit


prices=[3,4,7,1,55,45,12,34]
obj=Solution()
print(obj.maxProfit(prices))



#You are given an integer array prices where prices[i] is the price of a given stock on the i-th day.
#On each day, you may decide to buy and/or sell the stock.
#You can only hold at most one share at a time. However, you can buy and sell on the same day.
#Return the maximum profit you can achieve.

class Solution:
    def maxProfit2(self,prices2):
        i=0
        j=1
        profit=0
        while j<len(prices2):
            if prices2[j]>prices2[i]:
                profit=profit+prices2[j]-prices2[i]
            else:
                i=j
            j=j+1
        return profit
prices2=[3,4,7,1,55,45,12,34]
obj2=Solution()
print(obj2.maxProfit2(prices2))   

