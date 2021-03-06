"""
Lexicographically smallest string formed by removing at most one character.

Example 1:

Input: "abczd"
Output: "abcd"

"""

# Solution 1:
class Solution():
    def solution(self,S):
        for i in range(len(S)-1):
            if S[i] > S[i+1]:
                break
        return S[:i]+S[i+1:]


s = Solution()
assert s.solution("abczd") == "abcd"
print("pass all test case")


# Solution 2:
def lexi_smallest(s: str) -> str:
    """
    Time  : O(N)
    Space : O(N), where N = len(s)
    """
    # EDGE CASE
    if len(s) < 2:
        return ""

    # FIND THE CHAR THAT IS GREATER THAN ITS RIGHT NEIGHBOUR
    i = 0
    while i < len(s) - 1 and s[i] <= s[i + 1]:
        i += 1

    # ALL CHARS ARE IN ASCENDING ORDER
    return s[:i] + s[i + 1:] if i < len(s) - 1 else s[:-1]


if __name__ == "__main__":
    print(lexi_smallest("abczd") == "abcd")
    print(lexi_smallest("a") == "")
    print(lexi_smallest("aa") == "a")
    print(lexi_smallest("abc") == "ab")
    print(lexi_smallest("acb") == "ab")
    print(lexi_smallest("ba") == "a")
    print(lexi_smallest("bac") == "ac")
    print(lexi_smallest("bca") == "ba")
    print(lexi_smallest("cab") == "ab")
    print(lexi_smallest("cba") == "ba")