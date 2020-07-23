class Solution:
    def romanToInt(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        num_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                   'C': 100, 'D': 500, 'M': 1000}

        rslt = 0
        for i in range(len(s)):
            if i > 0 and num_map[s[i]] > num_map[s[i-1]]:
                rslt += num_map[s[i]] - (2 * num_map[s[i-1]])
            else:
                rslt += num_map[s[i]]

        return rslt

if __name__ == "__main__":
    r1 = 'IX'
    r2 = "MCM"
    r3 = 'L'
    sol = Solution()
    print(sol.romanToInt(r1))
    print(sol.romanToInt(r2))
    print(sol.romanToInt(r3))
