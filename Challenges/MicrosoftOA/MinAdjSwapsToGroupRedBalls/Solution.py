"""
Input: "RRRWRR"
Output: 2

"""

class Solution():
    def solution(self,S):
        R_index = []
        for i,v in enumerate(S):
            if v == 'R':
                R_index.append(i)
        mid = len(R_index) //2
        output = 0
        for i in range(len(R_index)):
            output += abs(R_index[mid] - R_index[i]) - abs(mid-i)
        print(output)
        if output > 10**9:
            return -1
        else:
            return output
s = Solution()

assert s.solution('WRRWWR') == 2
assert s.solution('WWRWWWRWR') == 4
assert s.solution('www') == 0
assert s.solution('RW'*4000000) == -1
print("pass all test case")

"""
Minimum swaps need to make k girls sitting together
Given a string contains only "B"s and "G"s indicated a sequence of students, while "B" means a boy and "G" means a girl. Write a function called minSwaps(students, k) to calculate the minimum swaps need to make k girls sitting together. Note that you could only swap two students if they are adjacent.

Example 1:

Input: students = "BGGBBG", k = 3
Output: 2

Example 2:

Input: students = "BGGBGBGBBGGG", k = 4
Output: 2

"""

