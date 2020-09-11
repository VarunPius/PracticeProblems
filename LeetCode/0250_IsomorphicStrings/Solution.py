class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        resultMap = {}
        t_set = set()

        for i in range(len(s)):
            if resultMap.get(s[i]):
                if resultMap[s[i]] != t[i]:
                    return False
            elif t[i] in t_set:
                return False
            else:
                resultMap[s[i]] = t[i]
                t_set.add(t[i])

        return True


def main():
    soln = Solution()
    print(soln.isIsomorphic("egg", "add"))

main()