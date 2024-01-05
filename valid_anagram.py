class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        wordDictS = {}
        wordDictT = {}
        for character in s:
            if character not in wordDictS:
                wordDictS[character] =1
            else:
                wordDictS[character]+=1
        for character in t:
            if character not in wordDictT:
                wordDictT[character] =1
            else:
                wordDictT[character]+=1
        return wordDictS == wordDictT


        