def gcd(a, b):
    if len(a) < len(b):
        short = a
        longg = b
    else:
        short = b
        longg = a
    pref = ""
    for x in range(1, len(short) + 1):
        if short.replace(short[:x], "") == "" and longg.replace(short[:x], "") == "":
            pref = short[:x]
    return pref


print(gcd("abcabc", "abc"))
print(gcd("ababab", "abab"))
print(gcd("leet", "code"))
