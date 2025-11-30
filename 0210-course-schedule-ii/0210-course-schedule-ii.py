from collections import defaultdict
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, p: List[List[int]]) -> List[int]:
        ind = defaultdict(int)
        adj = defaultdict(list)

        for [u, v] in p:
            ind[u] += 1
            adj[v].append(u)
        
        def _bfs(ind):
            q = deque()

            for i in range(numCourses):
                if ind[i] == 0:
                    q.append(i)

            res = []
            while q:
                u = q.popleft()
                res.append(u)

                for v in adj[u]:
                    ind[v] -= 1
                    if ind[v] == 0:
                        q.append(v)
            
            if len(res) != numCourses:
                return []
            return res
        
        return _bfs(ind)






        