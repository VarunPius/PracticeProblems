class Solution:
    # def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    def numRollsToTarget(self, d, f, target):
        memo = {}
        def dp(d, target):
            if d == 0:
                return 0 if target > 0 else 1
            if (d, target) in memo:
                return memo[(d, target)]
            to_return = 0
            for i in range(max(0, target - f), target):
                to_return += dp(d-1, i)
            memo[(d, target)] = to_return
            return to_return

        return dp(d, target) % (10**9 + 7)

    def numRollsToTarget2(self, d, f, t):
        mod = 1000000000 + 7
        dp = [[0 for i in range(t + 1)] for j in range(d)]
        print(dp)


if __name__ == '__main__':
    soln = Solution()
    #i = soln.numRollsToTarget(2, 6, 7)
    #print(i)
    soln.numRollsToTarget2(2, 6, 7)


