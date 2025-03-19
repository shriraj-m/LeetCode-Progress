"""338. Counting Bits"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for index in range(n+1):
            result.append(bin(index).count('1'))
        return result
    
    