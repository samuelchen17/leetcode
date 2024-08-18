class Solution:
    def isValid(self, s: str) -> bool:
        """
        without hashmap
        loop through the array
        if opening parentheses, add to stack
        if closing parentheses, check top of stack to see if match
        if match, pop the top and continue
        if not return false
        at the end of the array, check if stack is empty
        if empty, return true
        if not return false
        """

        stack = []

        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            # need to check if stack is empty first
            elif stack:
                if char == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif char == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                elif char == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
            else:
                return False

        return not stack
