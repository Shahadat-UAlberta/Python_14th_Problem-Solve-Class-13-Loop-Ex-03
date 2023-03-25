# break and continue

num = int(input())

for value in range(1, 11):
    if value == 2:
        continue
    if value <= 5:
        cal = num * value
        print(num, " X ", value, " = ", cal)
    else:
        break   