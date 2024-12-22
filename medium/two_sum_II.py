"""
### Intuition
    - we have to find the index of 2 numbers that the sum is equal to target
    - so my approach is loop through each number and look for other number in list
    - if target - (current_number_in_list) is exist in the list then return the index of that number
    - the time complexity is still high so there is room for improvement
"""


def twoSum(numbers: list[int], target: int) -> list[int]:
    for x in numbers:
        if target - x in numbers[numbers.index(x) + 1 :]:
            return [
                numbers.index(x) + 1,
                numbers[numbers.index(x) + 1 :].index(target - x)
                + numbers.index(x)
                + 2,
            ]
