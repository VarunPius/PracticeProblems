class Solution:
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    def combinationSum(self, candidates, target):
        result = []

        candidates.sort()
        self.dfs(result, candidates, target, [], 0)

        return result

    def dfs(self, result, candidates, target, path, idx):
        if target == 0:
            result.append(path)
            return

        if target < 0:
            return

        for i in range(idx, len(candidates)):
            self.dfs(result, candidates, target - candidates[i], path + [candidates[i]], i)


if __name__ == '__main__':
    soln = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    x = soln.combinationSum(candidates, target)
    print(x)
