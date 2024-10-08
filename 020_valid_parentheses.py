class Solution:
    def isValid(self, s: str) -> bool:
        # create a hashmap for checking bracket opening and closing
        # create a stack, and add opening brackets to the stack until reach closing bracket
        # use hashmap to check if the top of the stack is the opening parentheses for the closing
        # if yes, pop the stack
        # if not, return false
        # at the end, check if stack is empty, if empty return true, if false return false

        bracket_map = {")": "(", "]": "[", "}": "{"}
        stack = []

        # basically whenever we come across a closing parentheses, the top of stack must be the same
        for c in s:
            # check if this character is a closing parentheses
            if c in bracket_map:
                # check if parentheses is empty
                # and top of the stack is the same as the closing parentheses
                # stack[-1] is the last value added
                if stack and stack[-1] == bracket_map[c]:
                    stack.pop()
                # if dont match or empty, that means it parentheses dont match
                else:
                    return False

            # as long as it is open parentheses, can keep adding to stack
            else:
                stack.append(c)

        # only true if stack is empty, this means every opening parentheses has been matched
        return True if not stack else False
