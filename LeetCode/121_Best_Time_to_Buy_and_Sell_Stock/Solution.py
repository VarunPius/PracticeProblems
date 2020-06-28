class Solution:
    #def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices):
        if len(prices)<=1 or prices is None:
            return 0

        result = 0
        minVal = prices[0]
        for price in prices:
            result = max(result, price - minVal)
            minVal = min(minVal, price)

        return result


if __name__ == '__main__':
    soln = Solution()
    i = soln.maxProfit([7,1,5,3,6,4])
    print(i)