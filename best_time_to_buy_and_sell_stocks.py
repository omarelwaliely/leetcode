class Solution(object):
    def maxProfit(self, prices):
        l,r = 0,1
        maximum = 0
        maxLength = len(prices)
        while(r<maxLength):
            maximum = max(maximum,prices[r]-prices[l])
            if(prices[r]<prices[l]):
                l=r
            r+=1
        return maximum