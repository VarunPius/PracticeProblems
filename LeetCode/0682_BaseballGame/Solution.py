class Solution:
    # def calPoints(self, ops: List[str]) -> int:
    def calPoints(self, ops) -> int:
        # Time: O(n)
        # Space: O(n)
        stack = []
        for token in ops:
            if token == 'C':
                stack.pop()
            elif token == 'D':
                stack.append(stack[-1] * 2)
            elif token == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(token))
        return sum(stack)
