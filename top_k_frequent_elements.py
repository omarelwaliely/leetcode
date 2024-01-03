class Solution(object):
    def topKFrequent(self, nums, k):
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        result = [key for key, _ in frequency]
        return result[:k]