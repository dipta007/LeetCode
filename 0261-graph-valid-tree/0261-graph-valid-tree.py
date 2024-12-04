class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        from collections import defaultdict
        adj = defaultdict(list)
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        vis = [0] * n
        def call(u):
            vis[u] = 1

            for v in adj[u]:
                if vis[v] == 0:
                    call(v)
        
        call(0)

        # print(vis)
        return all(vis[x] == 1 for x in range(n))