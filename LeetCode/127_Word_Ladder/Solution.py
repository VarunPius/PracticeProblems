from collections import deque
import collections

class Solution:
    #def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    def ladderLength2(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words:
            return 0

        que = deque([(beginWord, 1)])
        while que:
            word, nos_of_steps = que.popleft()
            if word == endWord:
                return nos_of_steps
            for i in range(len(word)):
                for val in range(26):
                    #acii a = 97
                    newWord = word[:i] + chr(val + 97) + word[i+1:]
                    if newWord in words:
                        print(newWord)
                        words.remove(newWord)
                        que.append((newWord, nos_of_steps+1))
                    if word == endWord:
                        return nos_of_steps
        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newLayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    return len(layer[w][0])
                else:
                    for i in range(len(w)):
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            nw = w[:i] + c + w[i+1:]
                            if nw in wordList:
                                newLayer[nw] += [j + [nw] for j in layer[w]]
            wordList -= set(newLayer.keys())
            layer = newLayer
        return 0




def main():
    soln = Solution()
    i = soln.ladderLength("hit", "cog", ["hot","dot","dog","lot","log", "cog"])
    print(i)


if __name__ == '__main__':
    main()
