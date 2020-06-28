class Solution:
    #def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def groupAnagrams(self, strs):
        dic = {}
        for st in strs:
            key = tuple(sorted(st)) # Note1
            dic[key] = dic.get(key, []) + [st]
        return list(dic.values())


if __name__ == '__main__':
    soln = Solution()

'''
Note1:
If used without tuple, it results in a unhasble type list error. This is because list can't be used as key in dict.
'''

