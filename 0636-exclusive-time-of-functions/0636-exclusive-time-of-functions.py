class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        for i in range(len(logs)):
            logs[i] = logs[i].split(":")
            logs[i] = [int(logs[i][0]), logs[i][1], int(logs[i][2])]

        start = [-1] * n
        res = [0] * n
        stack = []

        for f, typ, t in logs:
            if typ == 'start':
                if stack:
                    res[stack[-1][0]] += t - stack[-1][1]
                stack.append([f, t])
            else:
                end_f = stack.pop()
                res[f] += (t - end_f[1] + 1)
                if stack:
                    stack[-1][1] = t + 1

            
        return res
        