class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        amt = 0
        while i < j:
            height = min(heights[i], heights[j])
            width = j - i
            amt = max(amt, height * width)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return amt
            