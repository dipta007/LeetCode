class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        bold = [0] * len(s)
        for w in words:
            start = s.find(w)
            while start != -1:
                for i in range(start, start + len(w)):
                    bold[i] = 1
                
                start = s.find(w, start + 1)
        
        res = ""
        bold_start = False
        for i in range(len(s)):
            if bold[i] and not bold_start:
                bold_start = True
                res += "<b>"
                res += s[i]
            elif not bold[i] and bold_start:
                bold_start = False
                res += "</b>"
                res += s[i]
            else:
                res += s[i]

        if bold_start:
            res += "</b>"
        
        return res