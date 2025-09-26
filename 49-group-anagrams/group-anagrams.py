class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        if len(strs) == 0:
            return [[""]]
        result = defaultdict(list)

        for st in strs:
            counter = [0]*26
            for c in range(len(st)):
                counter[ord(st[c])-ord('a')] +=1
            key = tuple(counter)
            result[key].append(st)
        return result.values()
