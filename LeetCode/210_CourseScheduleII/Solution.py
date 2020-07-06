from collections import defaultdict
from collections import deque


class Solution:
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # BFS
    def findOrder(self, numCourses, prerequisites):
        res = []
        count = 0
        d = defaultdict(set)
        neigh = defaultdict(set)

        for i in range(numCourses):
            d[i] = set()
        for prereq in prerequisites:
            d[prereq[0]].add(prereq[1])
            neigh[prereq[1]].add(prereq[0])

        que = deque([i for i in d if not d[i]])
        while que:
            node = que.popleft()
            res.append(node)
            count += 1
            for i in neigh[node]:
                d[i].remove(node)
                if not d[i]:
                    que.append(i)

        return res if count == numCourses else []

    # DFS
    def findOrder2(self, numCourses, prerequisites):
        dic = defaultdict(set)
        neigh = defaultdict(set)
        res = []
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        stack = [i for i in range(numCourses) if not dic[i]]

        while stack:
            node = stack.pop()
            res.append(node)

            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)

        return res if not dic else []



if __name__ == '__main__':
    soln = Solution()
    soln.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])