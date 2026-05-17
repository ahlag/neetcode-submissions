class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        parentheses = {'(': ')', '{': '}', '[': ']'}

        for char in s:

            if char in parentheses:
                stack.append(char)
            else:
                if not stack:
                    return False
                # print(stack)
                # print(len(stack))
                # if len(stack) == 0:
                #     return False
                starting_paranthesis = stack.pop()
                if char != parentheses[starting_paranthesis]:
                    return False

        return len(stack) == 0
        