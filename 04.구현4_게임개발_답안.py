N, M = map(int, input().split())
A, B, direction = map(int, input().split())

# 방문한 위치를 1로 알려주는 map과 실제 맵이 따로 필요한데, 그 이유는 나중에 4바퀴 돌고 뒤로 이동할 때 방문했던 위치는 다시 갈 수 있지만 바다라면 못가기 때문이다.
visit = [[0] * M for i in range(N)]
array = [list(map(int, input().split())) for _ in range(N)]

# 방문한 좌표는 방문처리
# 현재 좌표 방문처리
visit[A][B] = 1

# 방향 정의 --> '오답'과 다르게 하나의 리스트에 모두 정의
# [북, 동, 남, 서]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 왼쪽으로 회전하는 함수 정의
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
count = 1
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    next_A = A + dx[direction]
    next_B = B + dy[direction]
    
    # 회전한 이후 정면에 가보지 않은 칸이 존재하면 이동
    if array[next_A][next_B] == 0 and visit[next_A][next_B] == 0:
        visit[next_A][next_B] = 1
        A = next_A
        B = next_B
        count += 1
        turn_time += 1
        continue
    
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
        
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        next_A = A - dx[direction]
        next_B = B - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[next_A][next_B] == 0:
            A = next_A
            B = next_B
            
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
        
print(count)