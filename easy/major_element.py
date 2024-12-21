def majorityElement(nums: list) -> int:
    major = 0
    score = 0
    for x in set(nums):
        if nums.count(x) > score:
            score = nums.count(x)
            major = x
        print(f"major{major}")
        print(f"score{score}")
    return major


a = [-1, 100, 2, 100, 100, 4, 100]
print(majorityElement(a))
