class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea, i, j = 0, 0, len(height) - 1

        while i < j:
            maxArea = max(maxArea, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i +=1
            else:
                j -=1

        return maxArea

if __name__ == "__main__":
    height = [1, 2, 3, 4, 3, 2, 1, 5]
    result = Solution().maxArea(height)
    print(result)
