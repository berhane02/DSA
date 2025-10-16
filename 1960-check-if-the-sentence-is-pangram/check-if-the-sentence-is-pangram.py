class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        present = set()
        for c in sentence:
            present.add(c)
        return len(present) == 26