from collections import defaultdict

def getDistanceMetrics(arr):
    print(arr)
    result = [0]*len(arr)
    num_dict = {}

    for i, num in enumerate(arr):
        num = arr[i]
        if num not in num_dict:
            num_dict[num] = []
        num_dict[num].append(i)

    print(num_dict)

    for key in num_dict:
        lst = num_dict[key]
        if len(lst) > 1:
            for ele in lst:
                temp_lst = lst.copy()
                temp_lst.remove(ele)
                print(temp_lst)
                sum = 0
                for num in lst:
                    sum += abs(ele - num)
                result[ele] = sum

    print(result)




if __name__ == '__main__':
    arr = [1, 2, 2, 1, 5, 1]
    result = getDistanceMetrics(arr)

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getPotentialDomains' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY lines as parameter.
#

def getPotentialDomains(lines):
    result = []
    # Write your code here
    for line in lines:
        start1 = [i for i in range(len(line)) if line.startswith("http://", i)]
        start2 = [i for i in range(len(line)) if line.startswith("https://", i)]
        start = start1 + start2

        end1 = [i for i in range(len(line)) if line.startswith(".com", i)]
        end2 = [i for i in range(len(line)) if line.startswith(".org", i)]
        end3 = [i for i in range(len(line)) if line.startswith(".gov", i)]
        end = end1 + end2 + end3
        start.sort()
        end.sort()

        if len(start) == 0 or len(start) != len(end):
            continue
        loc = {}
        for i, _ in enumerate(start):
            # print(start)
            # print(end)
            loc[i] = [start[i], end[i] + 4]

        for idx in loc:
            strt, end = loc[idx]
            web = line[strt:end]
        web = web.split("//")[1]
        if web.startswith("www") or web.startswith("ww2") or web.startswith("web"):
            web = web[4:]

        print(web)
        result.append(web)
    result = set(result)
    result = list(result)
    result.sort()

    final = ""
    for website in result:
        final += website + ";"
    final = final[:-1]
    return final


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lines_count = int(input().strip())

    lines = []

    for _ in range(lines_count):
        lines_item = input()
        lines.append(lines_item)

    result = getPotentialDomains(lines)

    fptr.write(result + '\n')
    fptr.close()
