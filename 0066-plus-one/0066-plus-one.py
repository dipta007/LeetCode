class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 0
        for j in range(len(digits)-1, -1, -1):
            c = digits[j] + c + int(j == len(digits) - 1)
            digits[j] = c % 10
            c //= 10
        
        if c:
            digits = [c] + digits
        
        return digits