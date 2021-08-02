# 빨간구슬이 구멍에 빠지면 성공이지만, 파란구슬이 구멍에 빠지면 실패
# 빨간구슬과 파란구슬이 동시에 빠져도 실패이다.
# 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지를 출력

n,m = map(int,input().split())
data = [list(input()) for _ in range(n)]
rx,ry,bx,by = 0,0,0,0
for i in range(n):
    for j in range(m):
        if data[i][j] == 'R':
            rx,ry = i,j
        elif data[i][j] == 'B':
            bx,by = i,j
q = [(rx,ry,bx,by,0)]
visit = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
visit[rx][ry][bx][by] = 1
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def move(x,y,d):
    count = 0
    while data[x+dx[d]][y+dy[d]] != '#':
        x += dx[d]
        y += dy[d]
        count += 1
        if data[x][y] == 'O':
            return x,y,count
    return x,y,count

def solve():
    while q:
        rx, ry, bx, by, cnt = q.pop(0)
        if cnt >= 10:
            continue
        for i in range(4):
            nrx,nry,r_count = move(rx,ry,i)
            nbx,nby,b_count = move(bx,by,i)
            if data[nbx][nby] == 'O':
                continue
            if data[nrx][nry] == 'O':
                return cnt+1
            if nrx == nbx and nry == nby:
                if r_count > b_count:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if visit[nrx][nry][nbx][nby] == 0:
                q.append((nrx, nry, nbx, nby, cnt+1))
                visit[nrx][nry][nbx][nby] = 1
    return -1

print(solve())