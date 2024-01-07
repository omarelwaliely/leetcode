class Solution(object):
    def rob(self, nums):
        dp = []
        if len(nums)==1:
            return nums[0]
        dp.append(nums[0])
        dp.append(max(nums[0],nums[1]))
        for i in range(2,len(nums)):
            dp.append(max(dp[i-1],dp[i-2]+ nums[i]))
        return max(dp[len(nums)-1],dp[len(nums)-2])
