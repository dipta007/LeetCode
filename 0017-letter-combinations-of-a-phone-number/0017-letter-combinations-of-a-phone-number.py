class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        print(mapping)
        res = []
        def call(i, curr):
            if i == len(digits):
                nonlocal res
                if curr:
                    res.append(curr[:])
                return
            
            for c in mapping[int(digits[i])]:
                call(i+1, curr + c)
            
        call(0, "")
        return res