class Solution:
    # def dailyTemperatures(self, T: List[int]) -> List[int]:
    def dailyTemperatures(self, T):
        ans = [0]*len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                prev_idx = stack.pop()
                ans[prev_idx] = i - prev_idx

            stack.append(i)
            print("ans", ans)
            print("stack", stack)

        return ans


if __name__ == '__main__':
    soln = Solution()
    x = soln.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    # [1, 1, 4, 2, 1, 1, 0, 0]
    print(x)
