"""
### Intuition
    - Our goal is to find if the number in the list can be used to jump all the way to the end of the list
    - To do that, im having an idea of checking if our current number is bigger or equal to the length of the list
    - If our number is 0 and we dont have jump available, we are finish. We cant go to the end
"""


def canJump(nums: list) -> bool:
    if len(nums) <= 1:
        return True
    is_reached = False
    available_jump = 0
    for x in range(len(nums) - 1):
        if nums[x] >= len(nums[x + 1 :]):
            is_reached = True
            break
        if nums[x] == 0 and available_jump == 0:
            break
        elif nums[x] != 0 and nums[x] > available_jump:
            available_jump = nums[x]
        available_jump -= 1
    return is_reached
