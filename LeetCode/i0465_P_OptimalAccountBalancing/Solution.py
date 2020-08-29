class Solution:
    # def minTransfers(self, transactions: List[List[int]]) -> int:
    def minTransfers(self, transactions) -> int:
        return

"""
Solution 1: BFS
[By original author] This solution has been proved to be wrong. The following test cases does not pass

ransactions = [
[6, 0, 50],
[1, 6, 40],
[2, 6, 10],
[6, 3, 40],
[6, 4, 10],
[5, 6, 25]
]

[Original post]
First step is quite clear. We need to exclude those people who ends up not owing or owed money.

Then we will have an array of non-zero numbers, which sums to be zero. For example

[4, -2, -2, 6, -6]

This can be converted into finding the minimal clique such that the elements sum up to be zero. Minimal means there is no subset which sums up to zero. In the example above, there are two minimal such cliques.

[4, -2, -2] and [6, -6]

The beautiful part of those cliques are that we only need to resolve the balance inside the clique. There will be no inter-clique transactions.

The final number of transactions will be 5 - 2, which is num_non_zero - num_clique.

To find the minimal clique is the perfect problem to be solved by BFS. We will start with one element in the set as the root, find the minimal length path in the tree which sum up to be zero. Remove that zero sum set and pick another root.

class Solution(object):
    def minTransfers(self, transactions):
        # :type transactions: List[List[int]]
        # :rtype: int
        def remove_one_zero_clique(non_zero):
            n = len(non_zero)
            q = collections.deque()            
            # q store ([index set], sum of set)
            q.append(([0], non_zero[0]))
            min_zero_set = None

            while q:
                cur_set, cur_sum = q.popleft()
                if cur_sum == 0:
                    min_zero_set = cur_set
                    break
                for j in range(cur_set[-1] + 1, n):
                    q.append((cur_set + [j], cur_sum + non_zero[j]))
            
            min_zero_set = set(min_zero_set)
            return [non_zero[i] for i in range(n) if i not in min_zero_set]
        
        
        bal = collections.defaultdict(int)
        for t in transactions:
            bal[t[0]] -= t[2]
            bal[t[1]] += t[2]
        non_zero = [bal[k] for k in bal if bal[k] != 0]
        
        bal_cnt = len(non_zero)
        while len(non_zero) > 0:
            non_zero = remove_one_zero_clique(non_zero)
            bal_cnt -= 1
        return bal_cnt
"""

"""
Solution 2: Short O(N * 2^N) DP solution with detailed explanation and complexity analysis
First, we need to exclude those people who ends up not owing or owed money.

Then we will have an array of non-zero numbers, which sums to be zero. For example:
[4, -2, -2, 6, -6]

Then the problem can be converted to the following:
    Given N accounts/persons who have non zero amounts,
    find the M = max number of sets where each set s has sum(s)==0.
    Each of these sets must be min_set. In other words, min_set CANNOT be divided to setA and setB where sum(setA) == sum(setB)==0.

And the answer would be N - M. Why?
Let's see an example: [-2, 2, -7, 3, 4]
Say we have N = 5, M=2.
set1 = {-2, 2}, set2 = {-7,3,4}
Let n1 = len(set1) = 2, and n2 = len(set2) = 3.
Because both set1 and set2 are min_set, we have:

    For set1, we need n1 - 1 = 1 transaction to settle the debt.
    For set2, we need n2 - 1 = 2 transactions to settle the debt.

Then we are done, we don't need any other transactions.
So in other words, for each min_set we need len(min_set) - 1 transaction to settle the debt.
Then we have:

ans = (transactions for min_set1) + (transactions for min_set2) + ... + (transactions for min_setm)
ans = len(min_set1) - 1 + len(min_set2) - 1 + ... + len(min_setm) - 1
Note: len(min_set1) + len(min_set2) + ... + len(min_setm) = N,
and there are M (-1)'s.
So we have ans = N - M.

Once this problem is converted to finding the max number of min_sets, you can solve it in multiple ways: DFS, backtracking, BFS, and so on.

Here I present a DP solution which has the benefit of simple implementation and easier complexity analysis.
The optimal substructure is as following:
Let set[mask] be the set of elements whose position is 1 in the mask.
For example: [-2, 2, -7, 3, 4], set[binary(10000)] = {-2}, set[binary(01010)] = {2, 3}.
Let dp[mask] be the maximum number of min_sets can be formed by the elements in set[mask].
Let sum[mask] be the sum of the elements in set[mask].
Let's define sub_mask as a binary number which has 1 less set_bit than mask. For example: binary(01010) is a sub_mask of binary(01110) , binary(00110) is also a sub_mask of binary(01110).
Then:

	if sum[mask] == 0:
		dp[mask] = max(dp[sub_mask] + 1) for all sub_masks.
	else:
		dp[mask] = max(dp[sub_mask]) for all sub_masks.

Implementation:

class Solution:
    def minTransfers(self, transactions):
        persons = collections.defaultdict(int)
        for sender, receiver, amount in transactions:
            persons[sender] -= amount
            persons[receiver] += amount
        
        amounts = [amount for amount in persons.values() if amount != 0]
        
        N = len(amounts)
        dp = [0] * (2**N) # dp[mask] = number of sets whose sum = 0
        sums = [0] * (2**N) # sums[mask] = sum of numbers in mask
        
        for mask in range(2**N):
            set_bit = 1
            for b in range(N):
                if mask & set_bit == 0:
                    nxt = mask | set_bit
                    sums[nxt] = sums[mask] + amounts[b]
                    if sums[nxt] == 0: dp[nxt] = max(dp[nxt], dp[mask] + 1)
                    else: dp[nxt] = max(dp[nxt], dp[mask])
                set_bit <<= 1
        
        return N - dp[-1]

Complexity Analysis:
Running Time: O(N * 2^N), there are 2^N subproblems, each subproblem contributes to O(N) larger problems.
Space: O(2^N)

Please upvote if you like it.

"""

"""
Solution 3: BFS
First we need to count the net balance for every person, we define it as the list "net".
The question is the same as finding the "loop" in a graph (which the sum of elements in each graph is 0), say, the answer is len(net) - number of circles.
Thus, in order to minimize the answer, we need to maximize the number of circle, so we need to let every circle become "smaller", which is the same as "shortest path in a circle", we can use BFS to solve it.

import collections
import Queue
class Solution(object):
    def minTransfers(self, transactions):
        def bfs(net):
            while q.qsize():
                t, path, start = q.get()
                if not t:
                    break
                for i in xrange(start, len(net)):
                    q.put((t+net[i], path+[i], i+1))
                    
            self.res += len(path)-1
            path = set(path)
            return [net[i] for i in xrange(len(net)) if i not in path]
            
        d = collections.Counter()
        for t in transactions:
            d[t[0]] += t[2]
            d[t[1]] -= t[2]
        net = [d[item] for item in d if d[item] != 0]
        
        self.res = 0
        while len(net):
            q = Queue.Queue()
            q.put((net[0], [0], 1))
            net = bfs(net)
        return self.res
        
        #bfs

"""