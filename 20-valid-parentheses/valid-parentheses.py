class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [s[0]]
        openBracket = ('(','[','{')
        #closeBracket = (')','}',"'])
        for i in range(1,len(s)):
            if s[i] in openBracket:
                stack.append(s[i])
            elif len(stack)>0 and (stack[-1] == '(' and s[i] == ')' or stack[-1] == '{' and s[i] == '}' or stack[-1] == '[' and s[i] == ']'):
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack) == 0