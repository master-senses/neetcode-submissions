from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_map = {}
        adj_list = defaultdict(list)
        visited = set()
        output = []

        # email_map logic
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_map[email] = name
            
            first = account[1]
            for email in account[2:]:
                adj_list[first].append(email)
                adj_list[email].append(first)

        print(adj_list)
        # return accounts
        def dfs(email, path):
            visited.add(email)
            path.append(email)

            for i in adj_list[email]:
                if i not in visited:
                    dfs(i, path)

        for email in email_map:
            if email not in visited:
                path = []
                dfs(email, path)
                path.sort()
                output.append([email_map[email]] + path)

        return output
            
            
            


