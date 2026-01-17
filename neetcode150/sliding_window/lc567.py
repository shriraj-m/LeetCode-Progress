class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # make a window size if s1 for s2
        # create a set for the window and compare.
        # note: cant use set, so sort instead
        if len(s1) > len(s2):
            return False

        s1_sorted = sorted(s1)
        l = 0
        r = len(s1)

        while r <= len(s2):
            temp_sorted = sorted(s2[l:r])
            if s1_sorted == temp_sorted:
                return True
            l += 1
            r += 1
        return False


