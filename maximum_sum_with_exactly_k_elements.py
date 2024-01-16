class Solution(object):
    def maximizeSum(self, nums, k):
        maximum = -1
        for num in nums:
            if num > maximum:
                maximum = num
        finalScore = 0
        for i in range(k):
            finalScore += maximum + i
        return finalScore