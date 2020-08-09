class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        startTimes = []
        endTimes = []

        for interval in intervals:
            startTimes.append(interval[0])
            endTimes.append(interval[1])

        room = 0

        startTimes.sort()
        endTimes.sort()

        while startTimes:
            st = startTimes.pop(0)
            et = endTimes[0]
            if st >= et:
                endTimes.pop(0)
            else:
                room += 1

        return room

    def minMeetingRooms2(self, intervals):
        timeline = []
        for i in intervals:
            timeline.append((i[0], 1))
            timeline.append((i[1], -1))

        timeline.sort()
        rslt = curr = 0

        for _, v in timeline:
            curr += v
            rslt = max(rslt, curr)

        return rslt


if __name__ == '__main__':
    soln = Solution()
    x = soln.minMeetingRooms2([[0, 30],[5, 10],[15, 20]])
    print(x)