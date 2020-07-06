class Trie:
    def __init__(self):
        self.sub = {}
        self.suggestion = []


class Solution:
    # def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    def suggestedProducts(self, products, searchWord):
        root = Trie()
        for product in products:
            self.insert(product, root)

        return self.check(searchWord, root)

    def insert(self, prod, root):
        trie = root

        for c in prod:
            if c not in trie.sub:
                trie.sub[c] = Trie()
            trie = trie.sub[c]
            trie.suggestion.append(prod)
            trie.suggestion.sort()
            if len(trie.suggestion) > 3:
                trie.suggestion.pop()

    def check(self, search, root):
        ans = []
        for c in search:
            if root:
                root = root.sub.get(c)
            ans.append(root.suggestion if root else [])

        return ans