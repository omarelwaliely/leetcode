class Solution(object):
    def isValid(self, s):
        stack = []
        opposites = {'}':'{', ']':'[', ')':'('}
        for character in s:
            if character in opposites:
                if not stack:
                    return False
                elif opposites[character]!= stack.pop():
                    return False
            else:
                stack.append(character)
        return not stack


        