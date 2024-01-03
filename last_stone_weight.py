import heapq # import not needed on leetcode
class Solution(object): #solution1 (sort on each loop)
    def lastStoneWeight(self, stones):
        while(len(stones)>1):
            stones.sort(reverse=True)
            if stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)
            else:
                stones[0] -= stones.pop(1)
        return stones[0] if len(stones) ==1 else 0

class Solution(object): #solution2 (heaps)
    def lastStoneWeight(self, stones):
        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone) #forcing max heap
        while(len(heap)>1):
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            if stone1 != stone2:
                heapq.heappush(heap, stone1-stone2)
        return -1*heap[0] if len(heap) ==1 else 0

        