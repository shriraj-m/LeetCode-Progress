"""1456. Maximum Number of Vowels in a Substring of Given Length"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou") 
        result = 0
        counter = 0

        # look at first window of k
        for idx in range(k):
            if s[idx] in vowels:
                counter += 1
        result = counter

        # slide window
        for i in range(k, len(s)):
            # check left side of window
            if s[i-k] in vowels:
                counter -= 1
            # check right side of window
            if s[i] in vowels:
                counter += 1
            # reset result 
            result = max(result, counter)
        
        return result