"""
### Intutition
    - so our goal is to check if a string is a palindrome
    - first we remove all non alphanumeric character
    - and then we check if the string is the same as reversed string
"""


def isPalindrome(s: str) -> bool:
    s = "".join(x for x in s.lower() if x.isalnum())
    if s == s[::-1]:
        return True
    return False
