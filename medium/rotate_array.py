"""
### Intuition
    - we have a goal to rotate the array k times.
    - i have an idea in mind which is we make a temporary array to solve the new rotated value
    - and we decide the new location of the value by adding the current position with the desired k, and modulus it with length of the list so we still in the range of the list index
    - after the whole temp list is filled which means the rotation is complete, we replace the nums list with our temp list
"""


def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    temp = [0] * len(nums)
    for x in range(len(nums)):
        new_position = (x + k) % len(nums)
        temp[new_position] = nums[x]
    nums[:] = temp[:]
