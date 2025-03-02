'''1768. Merge Strings Alternately'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        longword = word1 if len(word1) >= len(word2) else word2
        shortword = word1 if len(word1) < len(word2) else word2
        result = ""
        for index in range(len(shortword)):
            result += word1[index]
            result += word2[index]

        result += longword[len(shortword):]
        print(result)
        return result