import collections # import not needed on leetcode
class Solution(object):
    def numIslands(self, grid):
        def lookaround(r,c):
            q = collections.deque()
            q.append((r,c))
            grid[r][c] == "V"
            while(q):
                currR, currC = q.popleft()
                possibleMoves = [[currR,currC+1],[currR,currC-1], [currR+1,currC], [currR-1,currC]] #easier than doing 4 cases
                for newR, newC in possibleMoves:
                    if newR in range(rows) and newC in range(cols) and grid[newR][newC] == "1":
                        q.append((newR,newC))
                        grid[newR][newC] = "V"
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] == "1"):
                    lookaround(r,c)
                    count+=1
        return count
        


        