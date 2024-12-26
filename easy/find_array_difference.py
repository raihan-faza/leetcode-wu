class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer1 = []
        answer2 = []
        for x in set(nums1 + nums2):
            if x in nums1 and x not in nums2:
                answer1.append(x)
            elif x in nums2 and x not in nums1:
                answer2.append(x)
        return [answer1, answer2]
