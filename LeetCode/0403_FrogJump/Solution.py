class Solution:
    # def canCross(self, stones: List[int]) -> bool:
    def canCross(self, stones) -> bool:
        self.memo = set()
        target = stones[-1]
        stones = set(stones)

        ans = self.bt(stones, 1, 1, target)
        return ans

    def bt(self, stones, cur, speed, target):
        if (cur, speed) in self.memo:
            return False

        if cur == target:
            return True

        if cur > target or cur < 0 or speed <= 0 or cur not in stones:
            return False

        candidates = [speed - 1, speed, speed + 1]
        for c in candidates:
            if (cur + c) in stones:
                if self.bt(stones, cur + c, c, target):
                    return True

        self.memo.add((cur, speed))
        return False