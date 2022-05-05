# 파이썬에서 input()으로 받은 data는 리스트 형태로 저장됨
input_data = input()


# a1을 받았을 때, a를 1~8 숫자로 바꿔주기 위해 ord 사용
# ord/chr : 아스키코드 <-> 숫자 변환
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

step = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

count = 0

for case in step:
    # 이동하고자 하는 위치를 먼저 확인
    next_row = row + step[0]
    next_col = col + step[1]
    
    # 이동하고자 하는 위치로 이동이 가능하면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        count += 1
        
print(count)
    
    