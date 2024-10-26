class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a, b, c = float('inf'), float('inf'), float('inf')

        for v in nums:
            if v <= a:
                a = v
            elif v <= b:
                b = v
            else:
                return True
        
        return False