class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # look at a window of chars where atmost K are different than curr
        # if we see more than K different chars, we save and move our curr
        result = 0
        charset = set(s)
        print(charset)

        for c in charset:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                result = max(result, r - l + 1)
        return result
                

            