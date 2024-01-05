class Solution(object):
    def twoSum(self, nums, target):
        testDict = {}
        for index, num in enumerate(nums):
            if num in testDict:
                return [testDict[num], index]
            else:
                testDict[target-num] = index
        