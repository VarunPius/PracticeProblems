from collections import deque


class Solution:
    # def wallsAndGates(self, rooms: List[List[int]]) -> None:
    # BFS Solution:
    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return []

        r, c = len(rooms), len(rooms[0])
        q = deque()
        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    q.append([i, j])

        while q:
            i, j = q.popleft()
            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                if 0 <= i + x < r and 0 <= j + y < c and rooms[i + x][j + y] > rooms[i][j]:
                    rooms[i + x][j + y] = rooms[i][j] + 1
                    q.append([i + x, j + y])


"""
DFS Solution:
def wallsAndGates(self, rooms: List[List[int]]) -> None:
	def dfs(rooms, r, c, d):
            for x, y in [(-1,0), (1,0), (0,-1), (0,1)]:
                if 0 <= r+x < len(rooms) and 0 <= c+y < len(rooms[0]) and rooms[r+x][c+y] > rooms[r][c]:
                    rooms[r+x][c+y] = d + 1
                    dfs(rooms, r+x, c+y, d+1)
        
	if not rooms:
		return []
	for r in range(len(rooms)):
		for c in range(len(rooms[0])):
			if rooms[r][c] == 0:
				dfs(rooms, r, c, 0)
"""

"""
BFS Alternate solution:
First of all, we need to practice in order to get your brain being familiar with the idea: "bfs is the good choice".

We want to search the shortest distance from all empty room to the gate. BFS is inherently a shortest path search algorithm.
Second, there may be a case where an empty room can reach multiple gates. Hence, we need a comparison function that keep the smaller distance. Use min

Step 1:
insert all 0 position into the queue. that's where we begin our searching. The position would be like this: (i,j,step). The step for starting position is 0: (i,j,0).

Step 2:
As we proceed searching, image you search a tree level by level using bfs, at every step you increase the depth by 1 as we're going deeper down to the leaf node. It's the same here. As we search deeper, we add 1 to the step indicating the cost is increasing. step + 1

Step 3:
every time when we reach a valid position, we examine if the current cost + 1 is smaller than the cost already in this position.
A[r][c] = min(A[r][c], new_cost + 1)

Code:
    def wallsAndGates(self, rooms) -> None:
        # bfs - search from 0
        if not rooms:return
        rows,cols=len(rooms),len(rooms[0])
        q = collections.deque([])
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    q.append((i,j,0))
                    
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        visited = set()
        while q:
            row,col,step=q.popleft()
            for d in directions:
                r = row+d[0]
                c = col+d[1]
                if 0<=r<rows and 0<=c<cols and rooms[r][c] not in (-1,0):
                    rooms[r][c] = min(rooms[r][c], step+1)
                    if (r,c) not in visited:
                        q.append((r,c,rooms[r][c]))
                    visited.add((r,c))

"""