"""
Given a generic digital clock, having h number of hours and m number of minutes, the task is to find how many times the clock shows identical time.
The parameters were 4 integers A,B,C,D. The valid time should be somewhere between 00:00 and 24:00.
If the integers don't fulfil the requirements the function should return 0.

Restrictions: A,B,C,D are integers between [0,9]

public static int solve(int A, int B, int C, int D) {
//return the count of how many variants are there to combine the four integers so its a valid hour
// from 00:00 to 24:00
}

Testcase#1 (1,0,0,2) => (00:12) (00:21) (01: 02) (01:20) (02:10) (02:01) (10:02) (10:20) (12:00) (20:01) (20:10) (21:00) => should return 12
Testcase#2 (2,1,2,1) => should return 6
Testcase#3 (1,4,8,2) => should return 5
Testcase#4 (4,4,4,4) => should return 0
"""

import itertools


def correct_time(time):
    hours = time[0] * 10 + time[1]
    minutes = time[2] * 10 + time[3]
    return hours < 24 and minutes < 60


def hour_variation_count(a, b, c, d):
    count = 0
    for permutation in set(itertools.permutations([a, b, c, d])):
        if correct_time(permutation):
            count += 1
    return count

"""
def get_minutes(digits, i,j):
    return [ digits[c] for c in range(len(digits)) if c != i and  c != j ]

def is_valid_time(s, time):
    if ( (time[0]*10+time[1]) < 24 and (time[2]*10 + time[3]) < 60):
        s.add(tuple(time))

def main(digits):

    s = set()
    for i in range(len(digits)):
        for j in range(i+1, len(digits)):
            minutes = get_minutes(digits, i,j)
            time = [digits[i], digits[j]] + minutes
            is_valid_time(s,time)
            time = [digits[j], digits[i]] + [minutes[1], minutes[0]]
            is_valid_time(s,time)
            time = [digits[j], digits[i]] + minutes
            is_valid_time(s,time)
            time = [digits[i], digits[j]] + [minutes[1], minutes[0]]
            is_valid_time(s,time)         
    return len(s)



print(main([1,0,0,2]))
print(main([2,1,2,1]))
print(main([1,8,4,2]))
print(main([4,4,4,4]))
"""