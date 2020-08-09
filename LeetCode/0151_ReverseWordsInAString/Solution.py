from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        l = deque()
        #deque used: Check Question.py for notes

        tmp = ""
        for i in s:
            if i != " ":
                tmp += i
            elif len(tmp) != 0:
                l.appendleft(tmp)
                tmp = ""
        if len(tmp) != 0:
            l.appendleft(tmp)
        result = " ".join(l)
        return result


    def reverseWords2(self, s: str) -> str:
        i = 0
        for j in range(len(s)):
            if s[j] == " ":
                s = self.reverse(s, i, j - 1)
                i = j + 1
        s = self.reverse(s, i, len(s) - 1)
        s = self.reverse(s, 0, len(s) - 1)
        return s

    def reverse(self, word, left, right):
        list_str = list(word)
        while left < right:
            tmp = list_str[left]
            list_str[left] = list_str[right]
            list_str[right] = tmp
            left = left + 1
            right = right - 1
        word = ''.join(list_str)
        print(word)
        return word


def main():
    soln = Solution()
    print(soln.reverseWords("the sky is blue"))


if __name__ == "__main__":
    main()


#def reverseWords2(self, s: str) -> str:
#        return ' '.join(reversed(s.split()))
