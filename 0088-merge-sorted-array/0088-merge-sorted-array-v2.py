class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        h1, r2 = len(nums1) - 1, len(nums2) - 1
        r1 = m-1

        while r1 >= 0 and r2 >= 0:
            if nums1[r1] >= nums2[r2]:
                nums1[h1] = nums1[r1]
                h1 -= 1
                r1 -= 1
            else:
                nums1[h1] = nums2[r2]
                h1 -= 1
                r2 -= 1
        
        for i in range(r1, -1, -1):
            nums1[h1] = nums1[i]
            h1 -= 1
        for i in range(r2, -1, -1):
            nums1[h1] = nums2[i]
            h1 -= 1
        return nums1
