"""
    How do we form groups of M-aligned numbers?

    Let's run a quick example

    A = [-3, -2, 1, 0, 8, 7, 1]
    R = [0, 1, 1, 0, 2, 1, 1], where R[i] = A[i] % m

    How can we group the numbers?
    We have to ensure that all numbers in a group have the same remainder after dividing by m.
    Because if i % m == j % m, then (i - j) % m == 0, which satisfies our "M-aligned" criteria for the group.

    So, from R, we have...

    Group 1 = [-3, 0]       (Remainder = 0 after dividing any pair by m)
    Group 2 = [-2, 1, 7, 1] (Remainder = 1 after dividing any pair by m)
    Group 3 = [8]           (Remainder = 2 after dividing any pair by m)

    Since Group 2 has the largest size = 4, we return 4.


"""

from typing import List


def largest_m_aligned(arr: List[int], m: int) -> int:
    """
    Time  : O(N)
    Space : O(1), where N = len(arr)
    """

    # EDGE CASE
    if m == 0:
        return 0

    # LET REMAINDER[I] = HOW MANY NUMBERS HAVE REMAINDER OF I WHEN DIVIDED BY M
    remainders = [0] * m

    # COUNT THE POSSIBLE REMAINDERS
    for a in arr:
        remainders[a % m] += 1

    # DIFFERENCE OF ANY 2 NUMBERS WITH THE SAME REMAINDER AFTER DIVIDING BY M IS
    # GUARANTEED TO BE DIVISIBLE BY M
    # ie. if i % m == j % m --> (i - j) % m = 0
    return max(remainders)


if __name__ == "__main__":
    print(largest_m_aligned([-3, -2, 1, 0, 8, 7, 1], 3) == 4)  # [-2, 1, 7, 1]
    print(largest_m_aligned([7, 2, 4, 8, 6], 2) == 4)  # [2, 4, 6, 8]
    print(largest_m_aligned([3, 1, 4, 1, 5], 1) == 5)  # [3, 1, 4, 1, 5]
    print(largest_m_aligned([5, 5, 5, 5, 5], 0) == 0)  # []
    print(largest_m_aligned([4, 7, 10, 6, 9], 3) == 3)  # [4, 7, 10]

# https://www.geeksforgeeks.org/find-set-m-element-whose-difference-two-element-divisible-k/