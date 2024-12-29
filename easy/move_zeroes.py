def move_zeroes(a: list):
    count = 0
    while count < len(a) - a.count(0):
        if a[count] == 0:
            a.pop(count)
            a.append(0)
        else:
            count += 1


a = [0, 0, 0, 1, 3, 4, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 3]
move_zeroes(a)
print(a)
