from collections import deque
import sys
import collections

class Solution:
    def findLadders1(self, beginWord, endWord, wordList):
    #def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        result = []
        que = deque([])
        not_visited = set(wordList)

        if(endWord not in wordList):
            return []

        Node = []
        Node.append(beginWord)
        Node.append(0)  #length to get to endWord
        Node.append([beginWord])

        que.append(Node)
        minD = sys.maxsize

        while que:
            print(que)
            topNode = que.popleft()
            word = topNode[0]
            distance = topNode[1]
            partialList = topNode[2]

            for i in range(len(word)):
                for c in range (26):
                    ch = 97 + c
                    newWord = word[:i] + chr(ch) + word[i+1:]
                    if newWord == word:
                        continue

                    if newWord == endWord:
                        result.append(partialList + [newWord])
                        if distance <= minD:
                            minD = distance
                        else:
                            return result
                    if newWord in not_visited:
                        newNode = [newWord, distance + 1, partialList + [newWord]] # See Note 1
                        que.append(newNode)
                        not_visited.remove(newWord)
        return result

    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        result = []
        layer = collections.defaultdict()
        layer[beginWord] = [[beginWord]]

        while layer:
            newLayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    print(layer[w])
                    result = layer[w]
                else:
                    for i in range(len(w)):
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            newW = w[:i] + c + w[i+1:]

                            if newW in wordList:
                                newLayer[newW] += [j + [newW] for j in layer[w]] #See note 2:

            wordList -= set(newLayer.keys())
            layer = newLayer
        return result



def main():
    soln = Solution()
    #i = soln.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    i = soln.findLadders2("red", "tax", ["ted", "tex", "tax", "tad", "den", "rex", "pee"])
    print(i)


if __name__ == '__main__':
    main()

#[
# ['hit', 'hot', 'dot', 'dog', 'cog'],
# ['hit', 'hot', 'lot', 'log', 'cog']
#]
#[
# ["red","ted","tad","tax"],
# ["red","ted","tex","tax"],
# ["red","rex","tex","tax"]
#]

# Note1:
# If you manipulate it as partialList.append(value) or distance = distance + 1, it keeps adding up as:
# ['hit', 'hot', 'dot', 'lot', 'dog', 'log', 'cog']
# This is because from dot, lot and dog are one character apart and the changes are impacted in the inner most loop
# so avoid changing variables

# Note2:
# If instead of newLayer[newW] += [j + [newW] for j in layer[w]] you do newLayer[newW] = [j + [newW] for j in layer[w]]
# it won't add multiple path to same word in between:
# for eg:
# tex can be reached as red->ted->tex or red->rex->tex
# but instead it will replace the first with the second during loop run


