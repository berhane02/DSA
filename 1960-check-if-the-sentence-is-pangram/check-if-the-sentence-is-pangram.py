class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        present = set()

        for c in sentence:
            present.add(c)
        # alp = set('abcdefghijklmnopqrstuvwxyz')
        # dif = alp - present
        # print(len(present))
        return len(present) == 26