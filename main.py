lst = [1, 2, 3, 4, 5]

start = 0
end = len(lst)

while start < end:
    if start > 0:
        lst[start] = lst[start] + lst[start - 1]

    start += 1

print(lst)


