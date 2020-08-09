class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.rank = 0


class AutocompleteSystem:
    # def __init__(self, sentences: List[str], times: List[int]):
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.searchTerm = ""
        # 1. add historical data
        for i, sentence in enumerate(sentences):
            self.add(sentence, times[i])
        return

    def add(self, sentence, rank):
        node = self.root
        # 2. for each character in sentence
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        # 3. when last character is added,
        # make node.isEnd = True indicate that the current node is end of the sentence
        node.isEnd = True
        # 4. do -= because by negating, we can sort as ascending order later
        node.rank -= rank

    def search(self):
        res = []
        node = self.root
        path = ""
        for c in self.searchTerm:
            if c not in node.children:
                return res
            # 6. add each character to path variable, path will added to res when we found node.isEnd ==True
            path += c
            node = node.children[c]
        # 7. at this point, node is at the given searchTerm.
        # for ex. if search term is "i_a", we are at "a" node.
        # from this point, we need to search all the possible sentence by using DFS
        self.dfs(node, path, res)
        # 11. variable res has result of all the relevant sentences
        # we just need to do sort and return [1] element of first 3
        return [item[1] for item in sorted(res)[:3]]

    def dfs(self, node, path, res):
        # 8. Check if node is end of the sentence
        # if so, add path to res
        if node.isEnd:
            # 9. when add to res, we also want to add hot for sorting
            res.append((node.rank, path))
        # 10. keep going if the node has child
        # until there is no more child (reached to bottom)
        for c in node.children:
            self.dfs(node.children[c], path + c, res)

    # def input(self, c: str) -> List[str]:
    def input(self, c):
        if c != "#":
            # 5. if input is not "#" add c to self.searchTerm and do self.search each time
            self.searchTerm += c
            return self.search()
        else:
            self.add(self.searchTerm, 1)
            self.searchTerm = ""
        return

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

