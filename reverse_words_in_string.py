class Solution(object):
    def reverseWords(self, s):
        if " " in s:
            words = s.split(" ")
        else:
            return s
        new_words = []
        for word in words:
            word = word.replace(" ", "") 
            if not word == "":
                new_words.insert(0, word)
        final = " ".join(new_words)
        return final