class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cum = 1
        cums = [1]
        zeros = [0]
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != 0:
                cums.append(cums[-1] * nums[i])
            else:
                cums.append(cums[-1])
            zeros.append(zeros[-1] + int(nums[i] == 0))
        
        cums = cums[1:]
        zeros = zeros[1:]
        cums.reverse()
        zeros.reverse()

        pre = 1
        zero = 0
        res = []
        for i in range(len(nums)):
            if i+1 < len(nums):
                if zeros[i+1]:
                    res.append(0)
                else:
                    res.append(pre * cums[i+1])
            else:
                res.append(pre)

            pre *= nums[i]
            zero += int(nums[i] == 0)

        return res