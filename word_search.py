class Solution(object):
    def exist(self, board, word):
        path = set()
        def search(row, col, currInd):
            if currInd == len(word):
                return True
            if row >= r or col >= c or row < 0 or col < 0 or word[currInd] != board[row][col] or (row,col)  in path:
                return False
            path.add((row,col))
            newInd = currInd+1 #saves some time complexity
            result = search(row+1,col,newInd) or search(row-1,col,newInd) or search(row,col+1,newInd) or search(row,col-1,newInd)
            path.remove((row,col))
            return result
        r,c = len(board), len(board[0])
        for i in range(r):
            for j in range(c):
                if search(i,j,0):
                        return True