"""394. Decode String"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_string = ""
        k = 0

        for char in s:
            if char == "[":
                # just passed the integer, so save string and num
                stack.append(curr_string)
                stack.append(k)
                # reset values
                curr_string = ""
                k = 0
            elif char == "]":
                # segment complete, so get k and current string
                recent_k = stack.pop()
                recent_str = stack.pop()
                curr_string = recent_str + recent_k * curr_string
            elif char.isdigit():
                k = k * 10 + int(char)
            else:
                curr_string += char
        
        print(curr_string)
        return curr_string

