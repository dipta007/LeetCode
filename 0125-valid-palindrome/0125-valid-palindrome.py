class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        fs = []
        for c in s:
            if "a" <= c <= 'z' or '0' <= c <= '9':
                fs.append(c)
        s = "".join(fs)
        return s == s[::-1]