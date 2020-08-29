class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def days_from_1971(dt):
            year, mth, day = int(dt[:4]), int(dt[5:7]), int(dt[8:])

            for y in range(1971, year):
                if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
                    day += 366
                else:
                    day += 365

            if mth > 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                day += 1

            while mth - 1 > 0:
                mth -= 1
                day += monthDays[mth - 1]

            return day

        return abs(days_from_1971(date1) - days_from_1971(date2))
