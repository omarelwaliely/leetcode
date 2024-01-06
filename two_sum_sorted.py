class Solution(object): #two pointer
    def twoSum(self, numbers, target):
        l,r = 0, len(numbers)-1
        while(l<=r):
            if numbers[l]+numbers[r] > target:
                r-=1
            elif numbers[l]+numbers[r] < target:
                l+=1
            else:
                return [l+1,r+1]

class Solution(object): #hashmap
    def twoSum(self, numbers, target):
        wordDict = {}
        for i, num in enumerate(numbers):
            if num in wordDict:
                return [wordDict[num]+1, i+1]
            wordDict[target-num] = i