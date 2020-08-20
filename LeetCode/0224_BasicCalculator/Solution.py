class Solution:
    def calculate(self, s: str) -> int:
        ans, num, sign, stack = 0, 0, 1, []
        for x in s:
            if x.isdigit():
                num = 10*num + int(x)
            elif x in ["-", "+"]:
                ans += sign*num
                num = 0
                sign = [-1, 1][x == "+"] # sign = 1 if x=='+' else -1
            elif x == "(":
                stack.append(ans)
                stack.append(sign)
                sign, ans = 1, 0
            elif x == ")":
                ans += sign*num
                ans *= stack.pop()
                ans += stack.pop()
                num = 0
        return ans + sign*num
