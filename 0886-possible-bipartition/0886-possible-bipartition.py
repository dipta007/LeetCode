class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        from collections import defaultdict
        adj = defaultdict(list)
        ind = defaultdict(int)
        nodes = set()
        for [u, v] in dislikes:
            adj[u].append(v)
            adj[v].append(u)
            ind[v] += 1
            nodes.add(u)
            nodes.add(v)
        
        color = [-1] * 2004
        def dfs(u, c):
            color[u] = c
            ret = True
            for v in adj[u]:
                if color[v] != -1 and color[v] == c:
                    return False
                if color[v] != -1:
                    continue
                ret = ret and dfs(v, 1 - c)
            return ret

        
        nodes = list(nodes)
        res = True
        for i in range(1, n+1):
            if color[i] == -1:
                res = res and dfs(i, 0)
        return res
        


        