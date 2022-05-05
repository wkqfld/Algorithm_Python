N = int(input())
path = input().split()

x, y = 1, 1

for i in path:
    if i == "R":
        if x != 5:
            x += 1
        else:
            continue
    if i == "L":
        if x != 1:
            x -= 1
        else:
            continue
    if i == "U":
        if y != 1:
            y -= 1
        else:
            continue
    if i == "D":
        if y != 5:
            y += 1
        else:
            continue
    print("현재위치는 : ", y, x)
print("최종위치는 : ", y, x)
        
