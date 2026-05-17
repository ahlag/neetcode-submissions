class Solution:
    def isValid(self, s: str) -> bool:

        parentheses = {
            '[': ']',
            '{': '}',
            '(': ')'
        }

        stack = []

        for i in range(len(s)):

            if s[i] in parentheses:
                stack.append(parentheses[s[i]])
            elif not stack or s[i] != stack.pop():
                return False

        return not stack
        