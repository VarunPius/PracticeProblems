from typing import List


def day_of_week(day: List[int], k: int) -> str:
    """
    Time  : O(1)
    Space : O(1)
    """
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    day_num = {days[i]: i for i in range(len(days))}
    k %= 7
    return days[(day_num.get(day) + k) % len(days)]