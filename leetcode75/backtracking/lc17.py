"""17. Letter Combinations of a Phone Number"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(index, path):
            # since path must be same length as digits, since 1 value is 1 letter
            if len(path) == len(digits):
                combinations.append("".join(path))
                return
            
            # grabs characters associated with number in digits
            for char in letter_map[digits[index]]:
                path.append(char)
                backtrack(index+1, path)
                path.pop() # pop last letter 
            
        combinations = []
        backtrack(0, [])
        return combinations
