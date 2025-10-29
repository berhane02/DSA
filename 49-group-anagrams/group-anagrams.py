class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anag_map[sorted_word].append(word)
        return list(anag_map.values())