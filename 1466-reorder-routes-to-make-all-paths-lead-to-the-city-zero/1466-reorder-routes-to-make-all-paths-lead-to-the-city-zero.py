class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        from collections import defaultdict
        adj = defaultdict(list)
        
        for [u, v] in connections:
            adj[u].append((v, 1))
            adj[v].append((u, 0))

        vis = [0 for _ in range(n)]

        def dfs(u):
            vis[u] = 1

            res = 0
            for v, w in adj[u]:
                if vis[v] == 0:
                    res += w
                    res += dfs(v)

            return res

        return dfs(0)