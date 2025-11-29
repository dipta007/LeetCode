from collections import deque
import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        def _bfs(u):
            q = []
            heapq.heappush(q, (0, u))
            dist = [100000000] * (n+4)
            dist[u] = 0

            while len(q):
                d, u = heapq.heappop(q)
                for v, w in adj[u]:
                    if d + w < dist[v]:
                        dist[v] = d + w
                        heapq.heappush(q, (dist[v], v))
            
            for i in range(1, n+1):
                if dist[i] == 100000000:
                    return -1
            
            return max(dist[1:n+1])
        
        return _bfs(k)






        