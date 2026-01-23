class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for x in range(32):
            if (1 << x) & n:
                count += 1
        return count