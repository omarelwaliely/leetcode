class Solution(object):
    def isPerfectSquare(self, num):
        if num == 0 or num ==1:
            return True
        l,r = 0,num
        while(l<=r):
            m = (l + r) // 2
            cur = m*m
            if cur == num:
                return True
            elif num < cur:
                r = m-1
            else:
                l = m+1
        return False      