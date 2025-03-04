'''151. Reverse Words in a String'''

class Solution:
    def reverseWords(self, s: str) -> str:
        split_words = s.split()
        result = " ".join(split_words[::-1])
        return result
            