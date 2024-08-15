class Solution:
    def isValid(self, s: str) -> bool:
        # use hashmap to store the key value for ()
        #

        bracket_map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in bracket_map:
                if stack and stack[-1] == bracket_map[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        return True if not stack else False
