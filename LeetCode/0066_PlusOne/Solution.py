import math
import functools

class Solution:
    # def plusOne(self, digits: List[int]) -> List[int]:
    def plusOne1(self, digits):
        num = 0
        for i in range(len(digits)):
            num = num*10 + digits[i]
        return [int(i) for i in str(num + 1)]

    def plusOne(self, digits):
        num = functools.reduce(lambda x, y: x * 10 + y, digits) + 1
        return [int(i) for i in str(num)]

