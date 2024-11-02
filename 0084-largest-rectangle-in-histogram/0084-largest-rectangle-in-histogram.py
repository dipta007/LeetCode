class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        res = 0
        for i, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] > h:
                curr_h = heights[stack[-1]]
                stack.pop()
                curr_w = i - stack[-1] - 1
                curr_area = curr_h * curr_w
                res = max(res, curr_area)
            stack.append(i)
        
        while stack[-1] != -1:
            curr_h = heights[stack[-1]]
            stack.pop()
            curr_w = len(heights) - stack[-1] - 1
            curr_area = curr_h * curr_w
            res = max(res, curr_area)
        
        return res