class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == k:
            return sum(nums) / k
        start = 0
        end = k
        curravg = sum(nums[start:end])
        maxavg = curravg
        while end < len(nums):
            curravg = curravg - nums[start] + nums[end]
            if curravg > maxavg:
                maxavg = curravg
            start += 1
            end += 1

        return float(maxavg / k)
