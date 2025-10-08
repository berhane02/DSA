class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if len(s) != len(t):
        #     return False
        # # s1 = Counter(s)
        # # t1 = Counter(t)
        # # return s1 == t1
        # counter_s = [0]*26
        # counter_t = [0]*26

        # for i in range(len(s)):
        #     counter_s [ord(s[i])-ord('a')] +=1
        #     counter_t [ord(t[i])-ord('a')] +=1
        # return counter_s == counter_t

        return Counter(s) == Counter(t)
