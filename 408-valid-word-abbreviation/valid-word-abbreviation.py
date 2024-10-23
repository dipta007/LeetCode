class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        splitted_abbr = []
        num = 0
        for c in abbr:
            if c.isnumeric():
                if num == 0 and int(c) == 0:
                    return False
                num = num * 10 + int(c)
            else:
                if num:
                    splitted_abbr.append(num)
                    num = 0
                splitted_abbr.append(c)
        if num:
            splitted_abbr.append(num)

        i = 0
        for v in splitted_abbr:
            if isinstance(v, int):
                i += v
            else:
                if i < len(word) and word[i] == v:
                    i += 1
                else:
                    return False
        
        return i == len(word)
