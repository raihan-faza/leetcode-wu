def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    peta = {}
    for i, v in enumerate(nums):
        if v not in peta:
            peta[v] = i
        else:
            if abs(peta[v] - i) <= k:
                return True
            else:
                peta[v] = i
    return False
