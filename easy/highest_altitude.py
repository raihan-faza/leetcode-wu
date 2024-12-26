class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        tambah = 0
        for x in gain:
            tambah += x
            if tambah > alt:
                alt = tambah
        return alt
