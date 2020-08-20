from collections import defaultdict


class Solution:
    # def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    def accountsMerge(self, accounts):
        ans = []
        email_list_map = defaultdict(list)
        visited_accounts = [False]*len(accounts)
        for i, acc in enumerate(accounts):
            for j in range(1, len(acc)):
                email = acc[j]
                email_list_map[email].append(i)

        def dfs(x, emails):
            if visited_accounts[x]:
                return

            visited_accounts[x] = True
            for j in range(1, len(accounts[x])):
                email = accounts[x][j]
                emails.add(email)
                for neigh in email_list_map[email]:
                    dfs(neigh, emails)

        for i, acc in enumerate(accounts):
            if visited_accounts[i]:
                continue
            name, emails = acc[0], set()
            dfs(i, emails)
            ans.append([name] + sorted(emails))
            print("ans")

        return ans


if __name__ == '__main__':
    soln = Solution()
    x = soln.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]])
    print(x)


"""
We give each account an ID, based on the index of it within the list of accounts.

[
["John", "johnsmith@mail.com", "john00@mail.com"], # Account 0
["John", "johnnybravo@mail.com"], # Account 1
["John", "johnsmith@mail.com", "john_newyork@mail.com"],  # Account 2
["Mary", "mary@mail.com"] # Account 3
]
Next, build an emails_accounts_map that maps an email to a list of accounts, which can be used to track which email is linked to which account. This is essentially our graph.

# emails_accounts_map of email to account ID
{
  "johnsmith@mail.com": [0, 2],
  "john00@mail.com": [0],
  "johnnybravo@mail.com": [1],
  "john_newyork@mail.com": [2],
  "mary@mail.com": [3]
}
Next we do a DFS on each account in accounts list and look up emails_accounts_map to tell us which accounts are linked to that particular account via common emails. This will make sure we visit each account only once. This is a recursive process and we should collect all the emails that we encounter along the way.

Lastly, sort the collected emails and add it to final results, res along with the name.
"""