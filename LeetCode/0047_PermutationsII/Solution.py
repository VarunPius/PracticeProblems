class Solution:
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    def permuteUnique(self, nums):
        result = []
        self.dfs(result, nums, [])

        return result

    def dfs(self, result, nums, path):
        if not nums:
            if path not in result:
                result.append(path)

        for i in range(len(nums)):
            self.dfs(result, nums[:i] + nums[i + 1:], path + [nums[i]])
