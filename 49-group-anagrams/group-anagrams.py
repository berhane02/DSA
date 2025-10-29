class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_map = defaultdict(list)

        # for word in strs:
        #     sorted_word = ''.join(sorted(word))
        #     anag_map[sorted_word].append(word)
        # return list(anag_map.values())

        for w in strs:
            index = [0]*26
            for i in range(len(w)):
                index[ord(w[i])-ord('a')] +=1
            anag_map[tuple(index)].append(w)
        return list(anag_map.values())