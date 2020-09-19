class Solution:
    def widestPath(self, x, y):
        sortedX = sorted(x)
        difference = 0

        for i in range(0, len(sortedX) - 1):
            diff = sortedX[i + 1] - sortedX[i]
            if diff > difference:
                difference = diff
        return difference

print(Solution().widestPath([5, 5, 5, 7, 7, 7], [3, 4, 5, 1, 3, 7]))