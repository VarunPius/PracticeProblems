class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    def coinChange(self, coins, amount):
        dp = [0] + [float('inf') for _ in range(amount)]
        print(dp)

        for i in range(amount + 1):
            for c in coins:
                if i - c >=0:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        if dp[-1] == float('inf'):
            return -1
        return dp[amount]


if __name__ == '__main__':
    soln = Solution()
    x = soln.coinChange([1, 2, 5], 11)
    print(x)

