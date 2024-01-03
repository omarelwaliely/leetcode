class Solution(object):
    def maxArea(self, height):
        if len(height) == 0:
            return 0
        l, r = 0, len(height)-1
        maximum = min(height[l],height[r]) * (r-l)
        while(l<=r):
            maximum = max(min(height[l],height[r]) * (r-l), maximum)
            if height[l]>height[r]:
                r= r-1
            else:
                l= l+1
        return maximum
        