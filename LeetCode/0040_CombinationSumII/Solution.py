class Solution:
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    def combinationSum2(self, candidates, target):
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
            # Very important here! We don't use `i > 0` because we always want
            # to count the first element in this recursive step even if it is the same
            # as one before. To avoid overcounting, we just ignore the duplicates
            # after the first element.
            if i > idx and candidates[i] == candidates[i - 1]:
                continue

            # If the current element is bigger than the assigned target, there is
            # no need to keep searching, since all the numbers are positive
            if candidates[i] > target:
                break

            # We change the start to `i + 1` because one element only could
            # be used once
            self.dfs(result, candidates, target - candidates[i], path + [candidates[i]], i + 1 )

if __name__ == '__main__':
    soln = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    x = soln.combinationSum2(candidates, target)
    print(x)