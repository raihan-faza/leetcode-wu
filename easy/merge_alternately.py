class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shorter_word = word1 if len(word1) < len(word2) else word2
        longer_word = word1 if len(word1) > len(word2) else word2
        out = []
        for x in range(0, len(shorter_word)):
            out.append(word1[x])
            out.append(word2[x])
        out.append(longer_word[len(shorter_word) :])
        return "".join(x for x in out)
