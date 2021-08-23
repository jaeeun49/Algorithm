# 인접한 나라의 인구 차이가 L이상 R이하이면 하루동안 같은 연합이 된다.
# 같은 연합을 이루고 있는 각 칸은 (연합 인구수)/(연합의 총 칸의 개수) 만큼의 인구수가 된다.
# 인구이동이 며칠동안 발생하는지를 출력

n,l,r = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(i,j, index):
    union = []
    union.append((i,j))
    q = []
    q.append((i,j))
    count = 1
    total = data[i][j]
    check[i][j] = index

    while q:
        x,y = q.pop(0)
        for d in range(4):
            nx,ny = x+dx[d], y+dy[d]
            if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == -1: # 격자를 벗어나지 않고
                if l <= abs(data[x][y] - data[nx][ny]) <= r: # 인접한 나라의 인구 차이가 L이상 R이하 이면
                    check[nx][ny] = index
                    union.append((nx,ny))
                    q.append((nx,ny))
                    count += 1
                    total += data[nx][ny]
    for x,y in union:
        data[x][y] = total // count

day = 0
while 1:
    check = [[-1] * n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if check[i][j] == -1:
                bfs(i,j,day)
                count += 1
    if count == n*n:
        print(day)
        break
    day += 1