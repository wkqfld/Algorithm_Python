array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

table = [0] * (max(array) + 1)
print(table)

for i in array:
    table[i] += 1

for i in range(len(table)):
    for j in range(table[i]):
        print(i, end=" ")