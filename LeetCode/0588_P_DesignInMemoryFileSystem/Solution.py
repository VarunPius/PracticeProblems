import collections

Trie = lambda: collections.defaultdict(Trie)

class FileSystem:
    def __init__(self):
        self.fs = Trie
        self.filecontent = collections.defaultdict(str)

    # def ls(self, path: str) -> List[str]:
    def ls(self, path):
        if path in self.filecontent:
            return path.split("/")[-1]

        cur = self.fs
        for token in path.split("/"):
            if token in cur:
                cur = cur[token]
            elif token:
                return []

        return sorted(cur.keys())

    # def mkdir(self, path: str) -> None:
    def mkdir(self, path):
        cur = self.fs
        for token in path.split("/"):
            if token:
                cur = cur[token]

    # def addContentToFile(self, filePath: str, content: str) -> None:
    def addContentToFile(self, filePath, content):
        self.mkdir(filePath)
        self.filecontent[filePath] += content

    def readContentFromFile(self, filePath):
        return self.filecontent[filePath]


if __name__ == '__main__':
    ip = ["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
    op = [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
    soln = FileSystem()
    soln.mkdir("a")
    print(soln.ls("/a"))


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
