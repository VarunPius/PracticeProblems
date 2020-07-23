class Solution:
    #def trap(self, height: List[int]) -> int:
    def trap(self, height):
        sum = 0
        start = 0
        end = len(height) - 1
        leftMax = 0
        rightMax = 0

        while start < end:
            leftMax = max(leftMax, height[start])
            rightMax = max(rightMax, height[end])
            if leftMax < rightMax:
                sum += (leftMax - height[start])
                start += 1
            else:
                sum += (rightMax - height[end])
                end -= 1
        return sum


def main():
    soln = Solution()
    i = soln.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print(i)


if __name__ == '__main__':
    main()
