# 회전시키는 바퀴와 맞닿은 톱니의 극이 다르면 맞닿은 톱니는 반대방향으로 회전하게 된다.
# 톱니의 초기상태와 회전시키는 방법이 주어질때, 최종 톱니의 점수 합을 출력

from collections import deque
wheels = [deque(list(input())) for _ in range(4)]
k = int(input())
rotations = []
for _ in range(k):
    n,d = map(int,input().split())
    rotations.append((n-1, d))

for n,d in rotations:
    move = [0,0,0,0]
    move[n] = d

    # 오른쪽 방향 탐색
    i = n
    while i+1 <= 3:
        if wheels[i][2] != wheels[i+1][6]:
            move[i+1] = -move[i]
        i += 1

    # 왼쪽 방향 탐색
    i = n
    while 1 <= i:
        if wheels[i][6] != wheels[i-1][2]:
            move[i-1] = -move[i]
        i -= 1

    # 직접 회전시키기
    for index,turn in enumerate(move):
        wheels[index].rotate(turn)

print(sum([int(wheels[i][0]) * 2**i for i in range(4)]))