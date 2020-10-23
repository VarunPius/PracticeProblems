class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return


"""
Intuition
The intuition and quick methode is to find the final text result.
You can just use a string if you don't care cost on string modification.
Or you can use a stack or string builder to do it in O(N).

Use stack to avoid string modification.
Time O(N) and space O(N).

    def backspaceCompare(self, S, T):
        def back(res, c):
            if c != '#': res.append(c)
            elif res: res.pop()
            return res
        return reduce(back, S, []) == reduce(back, T, [])

"""

"""
Follow up: O(1) Space
Can you do it in O(N) time and O(1) space?
I believe you have one difficulty here:
When we meet a char, we are not sure if it will be still there or be deleted.

However, we can do a back string compare (just like the title of problem).
If we do it backward, we meet a char and we can be sure this char won't be deleted.
If we meet a '#', it tell us we need to skip next lowercase char.

The idea is that, read next letter from end to start.
If we meet #, we increase the number we need to step back, until back = 0

    def backspaceCompare(self, S, T):
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            while i >= 0 and (backS or S[i] == '#'):
                backS += 1 if S[i] == '#' else -1
                i -= 1
            while j >= 0 and (backT or T[j] == '#'):
                backT += 1 if T[j] == '#' else -1
                j -= 1
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i, j = i - 1, j - 1

"""