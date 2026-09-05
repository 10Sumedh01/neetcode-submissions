class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r,max_water = 0, len(heights) -1, 0

        while l < r :
            width = r - l
            h = min(heights[l],heights[r])
            max_water = max(max_water, width * h)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_water
        