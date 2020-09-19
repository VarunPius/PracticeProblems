def isStable(arr: List[int]) -> int:
    numStable = 0
    if len(arr) < 3:
        return 0
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            if arr[j + 1] - arr[j] == arr[i + 1] - arr[i]:
                # print(str(i) + "," + str(i+1) + "," + str(i+2))
                numStable += 1
            else:
                break
    return numStable if numStable < 1000000000 else -1


print(isStable([-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]))
print(isStable([]))

# 413 Arithmic slices
def numberOfArithmeticSlices(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    opt, i = [0,0], 1
    for j in range(2, len(A)):
        if A[j]-A[j-1] == A[j-1]-A[j-2]:
            opt.append(opt[j-1]+i)
            i += 1
        else:
            opt.append(opt[j-1])
            i = 1
    return opt[-1]