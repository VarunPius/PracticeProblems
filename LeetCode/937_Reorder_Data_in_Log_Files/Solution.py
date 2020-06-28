class Solution:
    #def reorderLogFiles(self, logs: List[str]) -> List[str]:
    def reorderLogFiles(self, logs):
        rslt = []
        numbers = []
        letters = []
        for log in logs:
            if log.split()[1].isdigit():
                numbers.append(log)
            else:
                letters.append(log)

        letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        rslt = letters + numbers
        return rslt

if __name__ == '__main__':
    soln = Solution()
    x = soln.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
    print(x)