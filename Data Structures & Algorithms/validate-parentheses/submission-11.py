class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                opening_bracket = stack.pop()
                if c == ')' and opening_bracket != "(":
                    return False
                elif c == '}' and opening_bracket != '{':
                    return False
                elif c == ']' and opening_bracket != '[':
                    return False
        if len(stack) > 0:
            return False
        else:
            return True