class Solution:
    # def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
    def prisonAfterNDays(self, cells, N):
        if not cells or N<=0:
            return cells
        patterns = set()
        cycle = 0

        def nextDay(cells):
            newcell = [0]*len(cells)
            for i in range(1, len(cells) - 1):
                newcell[i] = 1 if cells[i-1] == cells[i+1] else 0
            return newcell

        for i in range(N):
            next = nextDay(cells)
            # nextKey = [str(i) for i in next]
            # nextKey = "".join(nextKey)
            nextKey = str(next)
            if nextKey not in patterns:
                patterns.add(nextKey)
                cycle += 1
            else:
                break
            cells = next

        N%=cycle
        for i in range(N):
            cells = nextDay(cells)

        return cells


if __name__ == '__main__':
    soln = Solution()
    soln.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 12)