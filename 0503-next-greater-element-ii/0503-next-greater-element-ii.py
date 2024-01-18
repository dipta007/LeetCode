class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + nums

        st = []
        for i in range(len(nums)-1, -1, -1):
            v = nums[i]

            while st and st[-1] <= v:
                st.pop()
            nums[i] = st[-1] if st else -1
            st.append(v)
        return nums[:n]
            