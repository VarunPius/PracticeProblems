import heapq

class Solution:
    #def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    def kClosest(self, points, K):
        heap = []

        for point in points:
            x, y = point
            dist = -(x**2 + y**2)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [[x, y] for (dist, x, y) in heap]


if __name__ == '__main__':
    soln = Solution()
    x = soln.kClosest([[1,3],[-2,2]], 1)
    print(x)