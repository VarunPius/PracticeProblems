class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left = right = 0
        for c in S:
            if right == 0 and c == ")":
                left += 1
            else:
                right += 1 if c == "(" else -1
        return left + right
