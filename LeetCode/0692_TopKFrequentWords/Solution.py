from collections import Counter
import heapq


class Solution:
    #def topKFrequent(self, words: List[str], k: int) -> List[str]:
    def topKFrequent(self, words, k):
        res = []
        freqs = []

        counter = Counter(words)
        heapq.heapify(freqs)

        for word, count in counter.items():
            heapq.heappush(freqs, Word(count, word))
            if len(freqs) > k:
                heapq.heappop(freqs)

        for _ in range(k):
            res.append(heapq.heappop(freqs).word)

        return res[::-1]


class Word:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word   # Max Heap that's why > else we would have used <
        return self.count < other.count

    def __eq__(self, other):
        return self.count == other.count and self.word == other.word


if __name__ == '__main__':
    soln = Solution()
    x = soln.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is", "arun"], 4)
    print(x)