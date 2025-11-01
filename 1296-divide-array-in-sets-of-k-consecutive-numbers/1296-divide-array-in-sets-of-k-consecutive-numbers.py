class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        import heapq
        from collections import defaultdict
        if len(nums) % k != 0:
            return False

        subarr_sz = k
        heapq.heapify(nums)
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        
        while len(nums) > 0:
            mn = -1
            while mn == -1 and len(nums):
                curr = heapq.heappop(nums)
                if counter[curr] > 0:
                    mn = curr
                    counter[curr] -= 1
                    break
            
            if mn == -1: break
            
            curr_sz = 1
            while curr_sz < subarr_sz:
                mn += 1
                if counter[mn] == 0:
                    return False
                counter[mn] -= 1
                curr_sz += 1

            if curr_sz != subarr_sz:
                return False
        
        return True



                