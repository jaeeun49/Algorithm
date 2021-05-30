# 원숭이는 k번만 말처럼 움직일 수 있고, 그 외에는 인접한 칸(상하좌우)으로 움직인다.

dx_m = [0,1,0,-1]
dy_m = [1,0,-1,0]
dx_h = [-2,-2,-1,-1,1,1,2,2]
dy_h = [-1,1,-2,2,-2,2,-1,1]

# 격자판의 맨 위쪽 위에서 시작해서 맨 오른쪽 아래까지 가야한다.
# 격자판이 주어졌을때 원숭이가 최소한 동작으로 갈 수 있는 동작수의 최솟값을 출력
# 시작점에서 도착점까지 갈 수 없으면 -1 출력

k = int(input())
m, n = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]

from collections import deque
def bfs():
    q = deque()
    q.append((0,0,k))
    visit = [[[0 for _ in range(31)] for _ in range(m)] for _ in range(n)]
    while q:
        x,y,cnt = q.popleft()
        if x == (n - 1) and y == (m - 1):
            return visit[x][y][cnt]
        if cnt > 0:
            for i in range(8):
                nx,ny = x + dx_h[i], y + dy_h[i]
                if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0 and visit[nx][ny][cnt-1] == 0:
                    q.append((nx,ny,cnt-1))
                    visit[nx][ny][cnt-1] = visit[x][y][cnt] + 1

        for j in range(4):
            nx,ny = x + dx_m[j], y + dy_m[j]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0 and visit[nx][ny][cnt] == 0:
                q.append((nx, ny, cnt))
                visit[nx][ny][cnt] = visit[x][y][cnt] + 1

    return -1

print(bfs())