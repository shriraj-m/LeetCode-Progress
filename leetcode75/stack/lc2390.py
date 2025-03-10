"""2390. Removing Stars From a String"""    
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)

        result = "".join(stack)
        return result