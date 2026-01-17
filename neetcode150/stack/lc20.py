class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opened = ["(", "{", "["]
        # closed = [")", "]", "}"]
        for char in s:
            # check if opened or closed
            if char in opened:
                stack.append(char)
            else:
                # if stack is empty then return false
                if len(stack) == 0:
                    return False
                # check what the top of the stack is
                top = stack[-1]
                # make sure char is it's match
                if top == "(" and char == ")":
                    stack.pop()
                elif top == "{" and char == "}":
                    stack.pop()
                elif top == "[" and char == "]":
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


        