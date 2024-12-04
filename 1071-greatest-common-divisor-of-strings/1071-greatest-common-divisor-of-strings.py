class Solution:
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        if len(s2) < len(s1):
            return self.gcdOfStrings(s2, s1)

        for i in range(len(s1), 0, -1):
            if len(s2) % i != 0: continue
            if len(s1) % i != 0: continue
            
            s1_pre = s1[:i]

            ns1 = s1_pre * int(len(s1) // i)
            ns2 = s1_pre * int(len(s2) // i)

            if ns1 == s1 and ns2 == s2:
                return s1_pre

        return ""
