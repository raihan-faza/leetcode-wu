def reverseVowels(s: str):
    vowel = "aiueo"
    haha = [x for x in s[::-1] if x.lower() in vowel]
    out = list(s)
    for i, v in enumerate(out):
        if v.lower() in vowel:
            out[i] = haha.pop(0)
    return "".join(out)


print(
    reverseVowels(
        "IceCreamaaaaaaaaaaaaabbbbbbbbbbbsssssssssssnnnnnnzuiuiuiquqiuiuiauiaiuaiawL"
    )
)
