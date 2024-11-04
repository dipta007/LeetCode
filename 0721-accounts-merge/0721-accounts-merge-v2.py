class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        par = [i for i in range(len(accounts))]

        def find(i):
            if par[i] != i:
                par[i] = find(par[i])
            
            return par[i]

        def union(x, y):
            x_p = find(x)
            y_p = find(y)

            par[x_p] = y_p


        from collections import defaultdict
        adj = defaultdict(set)
        for a in accounts:
            par = a[1]
            for j in range(2, len(a)):
                adj[par].add(a[j])
                adj[a[j]].add(par)

        for p in adj.keys():
            adj[p] = list(adj[p])

        vis = defaultdict(int)

        def call(u):
            vis[u] = 1

            res = [u]
            for v in adj.get(u, []):
                if vis[v] == 0:
                    res += call(v)

            return res

        res = []
        for a in accounts:
            name = a[0]
            par = a[1]
            if vis[par] == 0:
                curr = call(par)
                res.append([name] + sorted(list(set(curr))))
            
        return res

        from collections import defaultdict
        res = defaultdict(list)
        done = [0] * len(accounts)
        for i in range(len(accounts)):
            emails1 = accounts[i][1:]

            for j in range(i+1, len(accounts)):
                if done[j]: continue
                emails2 = accounts[j][1:]

                common = set(emails1).intersection(set(emails2))
                if len(common) > 0:
                    union(i, j)

        emails = {}
        names = {}
        for i in range(len(accounts)):
            p = find(i)
            if p not in names:
                names[p] = accounts[i][0]
                emails[p] = []

            emails[p].extend(accounts[i][1:])

        accounts = []
        for p in names.keys():
            curr = [names[p]] + sorted(list(set(emails[p])))
            accounts.append(curr)

        return accounts