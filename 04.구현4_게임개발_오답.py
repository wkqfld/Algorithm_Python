N, M = map(int, input().split())
A, B, d = map(int, input().split())

map = [list(int, input().split()) for _ in range(N)]


count = 0
turn_time = 0
    
while True:
    if d == 0:
        dx, dy = -1, 0
    elif d == 1:
        dx, dy = 0, 1
    elif d == 2:
        dx, dy = 1, 0
    else:
        dx, dy = 0, -1

    # 다음에 갈 위치 지정
    next_A = A + dy
    next_B = B + dx
    
    if map[next_A][next_B] == 0:
        count += 1
        A = next_A
        B = next_B
    else:
        next_A = A
        next_B = B
        turn_time += 1
    
    if d == 3:
        d = 0
    else:
        d += 1
        
