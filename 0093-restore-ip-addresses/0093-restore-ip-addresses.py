class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        dp = [[-1] * 7 for _ in range(len(s) + 4)]

        @cache
        def call(i, times, curr):
            if times > 4 or i > len(s):
                return []
            if i == len(s):
                if times == 4:
                    dp[i][times] = [curr.strip('.')]
                else:
                    dp[i][times] = []
                return dp[i][times]
            
            # if dp[i][times] != -1:
            #     return dp[i][times]
            
            res = []
            if s[i] == '0':
                nw = call(i+1, times+1, curr + ".0")
                if len(nw):
                    res.extend(nw)
            else:
                num = 0
                for j in range(i, len(s)):
                    num = num * 10 + int(s[j])
                    if num <= 255:
                        nw = call(j+1, times+1, curr + f".{str(num)}")
                        if len(nw):
                            res.extend(nw)
                    else:
                        break

            dp[i][times] = res
            return res
        
        res = call(0, 0, "")
        return res