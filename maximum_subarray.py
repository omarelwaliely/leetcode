class Solution(object): #greedy
    def maxSubArray(self, nums):
        maximum = -9999999
        currMaximum = -9999999
        for num in nums:
            if currMaximum < num and currMaximum <0:
                currMaximum = num
            elif currMaximum >= 0:
                currMaximum += num
            maximum = max(currMaximum, maximum)
        return maximum