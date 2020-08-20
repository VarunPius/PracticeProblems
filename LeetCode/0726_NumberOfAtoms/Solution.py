from collections import defaultdict

class Solution:
    # def countOfAtoms(self, formula: str) -> str:
    def countOfAtoms(self, formula: str) -> str:
        dic, ele, stack, coeff, i, cnt = defaultdict(int), "", [], 1, 0, 0
        for c in formula[::-1]:
            if c.isdigit():
                cnt += (int(c) * (10**i))
                i += 1
            elif c == ")":
                stack.append(cnt)
                coeff *= cnt
                i = cnt = 0
            elif c == "(":
                coeff //= stack.pop()
                i = cnt = 0
            elif c.isupper():
                ele += c
                dic[ele[::-1]] += (cnt or 1) * coeff
                ele = ""
                i = cnt = 0
            elif c.islower():
                ele += c
        return "".join(k + str(v>1 and v or "") for k, v in sorted(dic.items()))


if __name__ == '__main__':
    soln = Solution()
    x = soln.countOfAtoms("H2SO4")
    print(x)