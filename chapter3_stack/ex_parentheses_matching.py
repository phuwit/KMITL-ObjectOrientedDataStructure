VALID_PARENTHESES = {"(": ")", "{": "}", "[": "]"}


class Solution:
    def isValid(self, s: str):
        stack = list()
        for char in s:
            stack.append(char)
            for key, value in VALID_PARENTHESES.items():
                if len(stack) >= 2 and stack[-2] == key and stack[-1] == value:
                    stack.pop()
                    stack.pop()
                    break

        if len(stack) == 0:
            return True
        return False

print(Solution().isValid('()'))
