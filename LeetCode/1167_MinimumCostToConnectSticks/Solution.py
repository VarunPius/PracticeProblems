import heapq

class Solution:
    # def connectSticks(self, sticks: List[int]) -> int:
    def connectSticks(self, sticks):
        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1:
            x, y = heapq.heappop(sticks), heapq.heappop(sticks)
            res += x + y
            heapq.heappush(sticks, x + y)

        return res


if __name__ == '__main__':
    soln = Solution()
    i = soln.connectSticks([2,4,3])
    print(i)

