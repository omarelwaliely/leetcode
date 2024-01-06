class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l, r = 0, 0
        length = 0
        testSet = set()
        while r < len(s):
            if s[r] not in testSet:
                testSet.add(s[r])
                r += 1
                length = max(length, r - l)
            else:
                testSet.remove(s[l])
                l += 1
        return length