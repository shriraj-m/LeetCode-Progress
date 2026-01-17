class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # loop through each position in S
        # while the letter exists in a set, remove it and then increment
        # if letter isnt in it then add and calc max.
        curr = 0
        result = 0
        charset = set()

        for pos in range(len(s)):
            while s[pos] in charset:
                charset.remove(s[curr])
                curr += 1
            charset.add(s[pos])
            result = max(result, pos - curr + 1)
        return result