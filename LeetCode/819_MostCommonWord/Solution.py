class Solution:
    #def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    def mostCommonWord(self, paragraph, banned):
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = 0
        d = {}
        res = ""
        for word in paragraph.lower().split():
            if word in banned:
                continue
            elif word in d:
                d[word] += 1
            else:
                d[word] = 1
            if count < d[word]:
                count = d[word]
                res = word
        return res