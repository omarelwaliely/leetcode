class Solution(object):
    def maximum69Number(self, num):
        numArray = [int(x) for x in str(num)]
        for i in range(len(numArray)):
            if numArray[i] == 6:
                numArray[i] = 9
                break
        numString = "".join(map(str, numArray))
        return int(numString)