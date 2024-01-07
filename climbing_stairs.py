class Solution(object): #dynamic programming
  def climbStairs(self, n):
        if n == 0 or n ==1:
            return 1
        fin = []
        fin.append(1)
        fin.append(1)
        for i in range(2,n+1):
            fin.append(fin[i-1]+fin[i-2])
        return fin[n]
  
class Solution(object): #prev1 and prev2
    def climbStairs(self, n):
        if n == 0 or n ==1:
            return 1
        less_one,less_two = 1,1
        for _ in range(n-1):
            temp = less_one
            less_one = less_one+less_two
            less_two = temp
        return less_one