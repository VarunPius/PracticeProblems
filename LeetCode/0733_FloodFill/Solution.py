class Solution:
    # def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        # DFS
        row_ct, col_ct = len(image), len(image[0])
        orig_color = image[sr][sc]
        def traverse(row, col):
            if (not (0 <= row < row_ct and 0 <= col < col_ct)) or image[row][col] != orig_color:
                return
            image[row][col] = newColor
            [traverse(row + x, col + y) for (x, y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]]

        if orig_color != newColor:
            traverse(sr, sc)

        return image


"""
BFS
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor: 
            q = collections.deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = newColor
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == old: 
                        q.append((x, y))
        return image

DFS
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        def dfs(i, j):
            image[i][j] = newColor
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                    dfs(x, y)
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor: 
            dfs(sr, sc)
        return image
"""