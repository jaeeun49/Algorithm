# 태울 승객은 현재위치에서 최단거리가 가장 짧은 승객을 고른다.
# 그런 승객이 여러명이면 그중 행, 열 번호가 가장 작은 승객을 고른다.
# 연료는 한 칸 이동할 때마다 1만큼 소모
# 한 승객을 목적지로 이동시키면 그 승객을 태워 소모한 연료 양의 두 배가 충전된다.
# 모든 승객을 데려다줄 수 있는지, 데려다줄 수 있으면 남은 연료의 양을 출력

from collections import deque

# 태울 손님을 찾는 bfs함수
def bfs(sx, sy, customers, fuel):
    if customers.get((sx,sy)) is not None:
        return sx,sy,fuel

    queue = deque()
    nque = deque()
    point = []
    queue.append((sx,sy))
    visit = [[0]*n for _ in range(n)]
    visit[sx][sy] = 1
    while 1:
        while queue:
            x,y = queue.popleft()
            for d in range(4):
                nx,ny = x+dx[d], y+dy[d]
                if 0 <= nx < n and 0 <= ny < n and data[nx][ny]==0 and visit[nx][ny]==0:
                    visit[nx][ny] = 1
                    if customers.get((nx,ny)) is not None:
                        point.append((nx,ny))
                    else:
                        nque.append((nx,ny))
        fuel -= 1
        if fuel < 0:
            return -1,-1,-1
        if point:
            point.sort()
            return point[0][0], point[0][1], fuel
        queue = nque
        nque = deque()


# 손님을 목적지까지 데려다주는 bfs
def bfs2(px, py, tx, ty, fuel):
    if px == tx and py == ty:
        return 0

    queue = deque()
    queue.append((px,py,0))
    visit = [[0]*n for _ in range(n)]
    visit[px][py] = 1
    while queue:
        x,y,cnt = queue.popleft()
        if fuel <= cnt:
            return -1
        for d in range(4):
            nx,ny = x+dx[d], y+dy[d]
            if 0 <= nx < n and 0 <= ny < n and data[nx][ny]==0 and visit[nx][ny]==0:
                visit[nx][ny] = 1
                if nx == tx and ny == ty:
                    return cnt+1
                queue.append((nx,ny,cnt+1))
    return -1


n, m, fuel = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
# 백준이 운전을 시작하는 칸의 행,열 번호
start_x, start_y = map(int, input().split())
start_x -= 1
start_y -= 1
customers = {}
for _ in range(m):
    a1, b1, a2, b2 = map(int, input().split())
    customers[(a1 - 1, b1 - 1)] = (a2 - 1, b2 - 1)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


while 1:
    px,py,fuel = bfs(start_x, start_y, customers, fuel)
    if fuel < 0:
        print(-1)
        break

    tx,ty = customers.get((px,py))
    count = bfs2(px,py,tx,ty,fuel)
    if count == -1:
        print(-1)
        break

    fuel += count
    del customers[(px,py)]
    if len(customers) == 0:
        print(fuel)
        break
    start_x = tx
    start_y = ty