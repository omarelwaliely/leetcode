class Solution(object):
    def groupAnagrams(self, strs):
        listDict = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in listDict:
                listDict[sorted_word] = [word]
            else:
                listDict[sorted_word].append(word)
        return list(listDict.values())