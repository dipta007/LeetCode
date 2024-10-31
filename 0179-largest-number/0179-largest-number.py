class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key

        def compare(a, b):
            ab = a + b
            ba = b + a
            
            for i in range(len(ab)):
                if ab[i] < ba[i]:
                    return -1
                if ab[i] > ba[i]:
                    return 1
            
            return 0

        nums = [str(x) for x in nums]
        nums.sort(key=cmp_to_key(compare), reverse=True)
        if nums[0] == '0':
            return "0"
        return "".join(nums)