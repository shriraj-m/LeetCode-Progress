"""392. Is Subsequence"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0

        while t_pointer < len(t):
            if len(s) == s_pointer:
                return True

            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                t_pointer += 1
            else:
                t_pointer += 1
            
        if s_pointer == len(s):
            return True
        else:
            return False