class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = []
        maxc = max(candies)
        for x in candies:
            if x + extraCandies >= maxc:
                out.append(True)
            else:
                out.append(False)
        return out
