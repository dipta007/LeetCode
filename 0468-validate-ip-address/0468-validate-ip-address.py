class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def check_i(s):
            if len(s) == 0:
                return False
            if s[0] == '0' and len(s) > 1:
                return False
            for c in s:
                if c.isnumeric() or c in '.':
                    continue
                return False

            if int(s) > 255:
                return False
            return True

        def check_h(s):
            if len(s) == 0 or len(s) > 4:
                return False

            for c in s:
                if c.isnumeric() or c in 'abcdef':
                    continue
                return False
            
            return True

        def check(s, v):
            s = s.lower()
            
            s = s.split("." if v == 4 else ":")
            if len(s) != v: return False

            if v == 4: return all(check_i(i) for i in s)
            if v == 8: return all(check_h(i) for i in s)
        
        if check(queryIP, 4): return "IPv4"
        elif check(queryIP, 8): return "IPv6"
        return "Neither"