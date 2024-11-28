class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        def dfs(u):
            ret = True
            for v in graph[u]:
                if v not in color:
                    color[v] = 0 if color[u] else 1
                    ret = ret and dfs(v)
                elif color[v] == color[u]:
                    return False

            return ret

        res = True
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                res = res and dfs(i)
        return res