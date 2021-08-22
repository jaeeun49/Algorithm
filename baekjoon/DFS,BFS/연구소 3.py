# 바이러스 m개를 활성 상태로 변경하려고 한다.
# 모든 빈 칸에 바이러스를 퍼뜨리는 최소시간을 출력
# 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우는 -1출력

from itertools import combinations
from collections import deque
from copy import deepcopy
n,m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
virus = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            virus.append((i,j,0))
candidates = combinations(virus, m)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(a, data):
    data = deepcopy(data)
    q = deque()
    q.extend(a)
    visit = [[0] * n for _ in range(n)]
    time = 0

    while q:
        x,y,cnt = q.popleft()
        data[x][y] = cnt + 1
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] != 1 and visit[nx][ny] == 0:
                q.append((nx,ny,cnt+1))
                visit[nx][ny] = 1
                if data[nx][ny] == 0: # 이동하려는 칸이 빈칸이면
                    time = cnt + 1
    for i in range(n):
        for j in range(n):
            if data[i][j] == 0:
                return -1
    return time

answer = 1e9
for candidate in candidates:
    # 각각의 상황에서 모든 빈 칸에 바이러스가 버지는 최소시간을 반환
    time = bfs(candidate, data)
    if time < answer and time != -1:
        answer = time

if answer != 1e9:
    print(answer)
else:
    print(-1)