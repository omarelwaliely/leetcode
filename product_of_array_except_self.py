class Solution(object): #using postfix prefix
    def productExceptSelf(self, nums):
        result = [1 for _ in nums]
        prefix = 1
        for i,_ in enumerate(nums):
            result[i] = result[i-1]*prefix
            prefix =nums[i]
        post = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= post
            post *= nums[i]
        return result