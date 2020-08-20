class Solution:
    # def nearestPalindromic(self, n: str) -> str:
    def nearestPalindromic(self, n: str) -> str:
        ans = None
        L = len(n)
        candidates = [str((10**x) + d) for x in (L-1, L) for d in (-1, 1)]
        print(candidates)

        prefix = int(n[:(L+1)//2])
        print(prefix)

        for i in map(str, (prefix - 1, prefix, prefix + 1)):
            cand = i + (i[:-1] if L%2 else i)[::-1]
            candidates.append(cand)
        print(candidates)

        def delta(nos):
            return abs(int(n) - int(nos))

        for cand in candidates:
            if cand != n and not cand.startswith("00"):
                if ans is None or delta(cand) < delta(ans) or (delta(cand) == delta(ans) and int(cand) < int(ans)):
                    ans = cand

        return ans


if __name__ == '__main__':
    soln = Solution()
    x = soln.nearestPalindromic("234567")
    print(x)

"""
Let's build a list of candidate answers for which the final answer must be one of those candidates. 
Afterwards, choosing from these candidates is straightforward.

If the final answer has the same number of digits as the input string S, then the answer must be the middle digits + (-1, 0, or 1) flipped into a palindrome. 
For example, 23456 had middle part 234, and 233, 234, 235 flipped into a palindrome yields 23332, 23432, 23532. 
Given that we know the number of digits, the prefix 235 (for example) uniquely determines the corresponding palindrome 23532, so all palindromes with larger prefix like 23732 are strictly farther away from S than 23532 >= S.

If the final answer has a different number of digits, it must be of the form 999....999 or 1000...0001, as any palindrome smaller than 99....99 or bigger than 100....001 will be farther away from S.
"""
