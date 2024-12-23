"""
### Intuition
    - goal is to check if string in s are matched with desired pattern
    - if the length if different then it must be false
    - i try to use hashmap to pair the pattern with the word in the string
    - if the word doesnt match with the value of the pattern in hashmap, then the pattern doesnt match
"""


def wordPattern(pattern: str, s: str) -> bool:
    a = [x for x in pattern]
    b = s.split()
    if len(a) != len(b):
        return False
    if len(set(a)) != len(set(b)):
        return False
    hashmap = dict(zip(a, b))
    for x in range(len(a)):
        if hashmap[a[x]] != b[x]:
            return False
    return True
