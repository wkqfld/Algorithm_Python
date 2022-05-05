n = int(input())

grade = [tuple(input().split()) for _ in range(n)]

asc_grade = sorted(grade, key = lambda grade: grade[1])

for i in range(n):
    print(asc_grade[i][0], end = " ")