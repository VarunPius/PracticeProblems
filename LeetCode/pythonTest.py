from collections import defaultdict
from collections import deque

class Solution(object):
    def twosum(self, noslist, target):
        dict = {}
        rslt = []
        for idx, nos in enumerate(noslist):
            val = target - nos
            if nos in dict:
                rslt = [dict[nos], idx]
                return rslt
            else:
                dict[val] = idx
        return rslt


def main():
    soln = Solution()
    i = soln.twosum([2, 6, 4, 5, 8], 13)
    print(i)


if __name__ == '__main__':
    main()
