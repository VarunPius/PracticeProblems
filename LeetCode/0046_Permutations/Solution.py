class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    def permute(self, nums):
        result = []
        self.dfs(result, nums, [])
        return result

    def dfs(self, result, nums, path):
        if not nums:
            result.append(path)

        for i in range(len(nums)):
            self.dfs(result, nums[:i] + nums[i+1:], path + [nums[i]])
