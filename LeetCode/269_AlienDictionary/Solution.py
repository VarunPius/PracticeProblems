from collections import deque

class Solution:
    def alienOrder(self, words):
        letters = [0 for _ in range(26)]
        map = {}
        for word in words:
            for ch in word:
                key = ord(ch) - ord('a')
                map[key] = set()

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for j in range(min(len(word1), len(word2))):
                ch1 = word1[j]
                ch2 = word2[j]
                if ch1 != ch2:
                    key1 = ord(ch1) - ord('a')
                    key2 = ord(ch2) - ord('a')
                    count = letters[key2]
                    if key2 not in map[key1]:
                        letters[key2] += 1
                        map[key1].add(key2)
                        break

        que = deque()
        res = ""
        for i in range(26):
            if(letters[i] == 0 and i in map):
                que.append(i)

        while que:
            nextup = que.popleft()
            res += chr(nextup + ord('a'))
            greaterset = map[nextup]
            for greater in greaterset:
                letters[greater] -= 1
                if letters[greater] == 0:
                    que.append(greater)

        if len(map) != len(res):
            return ""

        return res


if __name__ == '__main__':
    soln = Solution()
    i = soln.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
    print(i)
    i = soln.alienOrder(["z", "x", "z"])
    print(i)

