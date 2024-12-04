class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import defaultdict
        vis = defaultdict(int)

        deadends = set(deadends)
        if "0000" in deadends: return -1
        def get(lock):
            curr = ""
            for i in range(len(lock)):
                for j in [-1, 1]:
                    nw = int(lock[i]) + j
                    if nw < 0:
                        nw = 9
                    if nw > 9:
                        nw = 0
                    
                    nw = str(nw)
                    curr = lock[:i] + nw + lock[i+1:]
                    if curr not in deadends and vis[curr] == 0:
                        yield curr

        from collections import deque
        dq = deque()
        dq.append(("0000", 0))

        while len(dq):
            u, d = dq.popleft()

            if u == target:
                return d

            for v in get(u):
                vis[v] = 1
                dq.append((v, d+1))
        
        return -1