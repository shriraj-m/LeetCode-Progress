class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "/", "*"]
        for item in tokens:
            if item not in operations:
                # this is a number, add to stack
                stack.append(int(item))
            else: # is operation
                # grab two most recent numbers
                num2 = stack.pop()
                num1 = stack.pop()

                if item == "+":
                    result = num1 + num2
                    stack.append(result)
                elif item == "-":
                    result = num1 - num2
                    stack.append(result)
                elif item == "/":
                    result = int(num1 / num2)
                    print(result)
                    stack.append(result)
                else: # "*"
                    result = num1 * num2
                    stack.append(result)
        return stack[-1]

        