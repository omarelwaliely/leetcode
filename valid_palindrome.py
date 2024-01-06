class Solution(object):
    def isPalindrome(self, s):
        s = "".join(filter(str.isalnum, str(s)))
        s = s.lower()
        length = len(s)
        if length==0:
            return True
        for i, _ in enumerate(s):
            j = length - i - 1
            if i >= j:
                return True
            elif s[i] != s[j]:
                return False