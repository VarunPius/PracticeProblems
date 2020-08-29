from collections import defaultdict


class Solution:
    # def numTeams(self, rating: List[int]) -> int:
    def numTeams(self, rating) -> int:
        if len(rating) < 3:
            return 0
        greater = defaultdict(int)
        lesser = defaultdict(int)
        ans = 0

        for i in range(len(rating) - 1):
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    greater[i] += 1
                else:
                    lesser[i] += 1

        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    ans += greater[j]
                else:
                    ans += lesser[j]

        return ans
