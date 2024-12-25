class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        p = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1 or n == 0:
                return True
            else:
                return False
        for i, v in enumerate(flowerbed):
            if i == 0:
                if v == 0 and flowerbed[i + 1] == 0:
                    p += 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0 and v == 0:
                    p += 1
            elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and v == 0:
                p += 1
                flowerbed[i] = 1
            if p >= n:
                return True
        return False
