class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in mapping.values():  # opening bracket
                stack.append(ch)
            elif ch in mapping:         # closing bracket
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
            else:
                return False  # invalid character

        return not stack