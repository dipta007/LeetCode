class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        from collections import defaultdict
        adj = defaultdict(list)

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        for k in adj.keys():
            adj[k] = set(adj[k])

        leaves = []
        for k in adj.keys():
            if len(adj[k]) == 1:
                leaves.append(k)
            
        rem = n
        while rem > 2:
            new_leaves = []
            rem -= len(leaves)

            for leave in leaves:
                neighbour = adj[leave].pop()
                adj[neighbour].remove(leave)
                if len(adj[neighbour]) == 1:
                    new_leaves.append(neighbour)

            leaves = new_leaves
        
        return leaves