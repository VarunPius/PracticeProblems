from collections import defaultdict
from itertools import combinations

class Solution:
    # def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
    def mostVisitedPattern(self, username, timestamp, website):
        by_user = defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            by_user[u].append(w)

        comb_dict = defaultdict(int)
        for web_list in by_user.values():
            print(web_list)
            combs = set(combinations(web_list, 3))
            print(combs)
            for comb in combs:
                comb_dict[comb] += 1

        sorted_dict = sorted(comb_dict, key=lambda x: (-comb_dict[x], x))
        return sorted_dict[0]


if __name__ == '__main__':
    soln = Solution()
    username = ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"]
    timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    website = ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]

    x = soln.mostVisitedPattern(username, timestamp, website)
    print(x)
