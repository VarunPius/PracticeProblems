import collections


class FreqStack:
    def __init__(self):
        self.freq = collections.Counter()
        self.stack = collections.defaultdict(list)
        self.maxf = 0

    def push(self, x: int) -> None:
        self.freq[x] += 1
        self.maxf = max(self.maxf, self.freq[x])
        self.stack[self.freq[x]].append(x)

    def pop(self) -> int:
        ans = self.stack[self.maxf].pop()
        if not self.stack[self.maxf]: self.maxf = self.maxf - 1
        self.freq[ans] -= 1
        return ans

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()


"""
Hash map freq will count the frequence of elements.
Hash map m is a map of stack.
If element x has n frequence, we will push x n times in m[1], m[2] .. m[n]
maxfreq records the maximum frequence.

push(x) will push x tom[++freq[x]]
pop() will pop from the m[maxfreq]
"""