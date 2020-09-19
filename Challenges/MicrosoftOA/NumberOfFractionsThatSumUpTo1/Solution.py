"""
Looks like a 2Sum problem. Time complexity O(n) space complexity O(n)

import collections
from math import gcd


def do2Sum(top, base):
    # Similar to how we store the target-num in 2Sum problem
    seen_dict = collections.defaultdict(int)
    pair = 0
    for i, j in zip(top,base):
        if i <= j:
            # to simplify the divisions like 2/10 into 1/5
            divisor = gcd(i,j)
            i = i/divisor
            j = j/divisor
            # check if we have seen the (1 - i/j) in dict
            if (j-i)/j in seen_dict:
                pair += seen_dict[((j-i)/j)]
            # update the dict with i/j count
            seen_dict[i/j] += 1
    return pair

def main():
    test_cases = {
        "test_1": [[1,1,2],[3,2,3]],
        "test_2": [[1,1,1],[2,2,2]],
        "test_3": [[1,2,3,1,2,12,8,4],[5,10,15,2,4,15,10,5]]
    }

    for key,val in test_cases.items():
        res = do2Sum(val[0], val[1])
        print(f'Result of {key} is {res}')

if __name__ == "__main__":
    main()

"""