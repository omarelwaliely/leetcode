class Solution(object):
    def minCostClimbingStairs(self, cost):
        length = len(cost)
        dp = [0] * (length + 1)
        dp[length-1] = cost[length-1]
        dp[length-2] = cost[length-2]
        for i in range(length-3, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        return min(dp[0], dp[1])