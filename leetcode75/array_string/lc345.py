''' 345. Reverse Vowels of a String '''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [l for l in s if l.lower() in "aeiou"]
        result = [l if l.lower() not in "aeiou" else vowels.pop() for l in s]
        
        new_s = "".join(result)
        return new_s

        