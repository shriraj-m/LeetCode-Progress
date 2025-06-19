class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case
        if len(s) != len(t):
            return False

        new_s = []
        new_t = []
        # length is the same
        for x in range(len(s)):
            new_s.append(s[x])
            new_t.append(t[x])
        
        new_s.sort()
        new_t.sort()

        if new_s == new_t:
            return True
        else:
            return False