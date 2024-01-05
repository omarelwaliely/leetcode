class Solution(object):
    def containsDuplicate(self, nums):
        testSet = set()
        for num in nums:
            if num in testSet:
                return True
            testSet.add(num)
        return False
        