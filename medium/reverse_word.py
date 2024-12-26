class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        return "".join(x + " " for x in a[::-1]).strip()
