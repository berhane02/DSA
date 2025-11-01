class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        max_len = 0
        start = 0

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[start])
                start +=1
            seen.add(s[i])
            max_len = max(max_len, len(seen))
        return max_len
        