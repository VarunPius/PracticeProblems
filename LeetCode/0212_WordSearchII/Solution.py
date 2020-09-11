from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord


class Solution:
    #def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    def findWords(self, board, words):
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)

        result = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, result, "", i, j)

        return result

    def dfs(self, board, node, result, path, i, j):
        if node.isWord:
            result.append(path)
            node.isWord = False

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return

        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return

        board[i][j] = "#"

        self.dfs(board, node, result, path + tmp, i+1, j)
        self.dfs(board, node, result, path + tmp, i-1, j)
        self.dfs(board, node, result, path + tmp, i, j+1)
        self.dfs(board, node, result, path + tmp, i, j-1)
        board[i][j] = tmp

