"""
## Intuition
    - so we have to take m number from list1 and n number from list 2 and they have to be sorted. The problem also state that dont return anything just replace the first array in place.

to solve this problem im thinking about several steps:
    - change list1 and list2 length to the value of number that we want to take
    - after we change it there is several ways that i can think of, number 1 we join the list and re-sort it. The complexity maybe O(nlogn)? (gotta check that out)
    - number 2 we use two for loop to find the place of the number that we will, maybe the complexity will be (n * m)
"""


def merge_sorted_array(list1: list, list2: list, m: int, n: int) -> None:
    list1[:] = (
        list1[:m] if len(list1) >= m else []
    )  # This is a way to modify list in place, nice info
    list2[:] = list2[:n] if len(list2) >= m else []
    list1.extend(list2)  # Merge the list
    list1.sort()  # Re-sort them


a = [1, 2, 3, 0, 0, 0]
b = [2, 5, 6]
m = 3
n = 3
merge_sorted_array(a, b, m, n)
print(a)
