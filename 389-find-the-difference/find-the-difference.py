class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # char_count = Counter(s)
      
        # # Iterate through each character in string t
        # for char in t:
        #     # Decrement the count for this character
        #     char_count[char] -= 1
          
        #     # If count becomes negative, this is the extra character added to t
        #     if char_count[char] < 0:
        #         return char

        c = 0
        for cs in s: c^= ord(cs)
        for ct in t: c^= ord(ct)
        return chr(c)