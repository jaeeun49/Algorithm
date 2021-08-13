# cctv는 cctv를 통과할 수 있다.
# cctv의 방향을 조절해서 감시할 수 없는 영역의 최소크기를 출력

n,m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,1,0,0] # 상하우좌
dy = [0,0,1,-1]

def watch(x,y,directions):
    c = set()
    for d in directions:
        nx,ny = x,y
        while 1:
            nx += dx[d]
            ny += dy[d]
            if not (0 <= nx < n and 0 <= ny < m): break
            if data[nx][ny] == 6: break
            if data[nx][ny] == 0:
                c.add((nx,ny))
    return c

max_watch = 0
def dfs(count, set):
    global max_watch
    if count == len(all_case):
        max_watch = max(max_watch, len(set))
        return

    for a in all_case[count]:
        dfs(count+1, set|a)

safe_zone = 0
all_case = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            safe_zone += 1
        elif data[i][j] == 1:
            all_case.append([watch(i,j,[0]), watch(i,j,[1]), watch(i,j,[2]), watch(i,j,[3])])
        elif data[i][j] == 2:
            all_case.append([watch(i,j,[0,1]), watch(i,j,[2,3])])
        elif data[i][j] == 3:
            all_case.append([watch(i,j,[0,2]), watch(i,j,[2,1]), watch(i,j,[1,3]), watch(i,j,[3,0])])
        elif data[i][j] == 4:
            all_case.append([watch(i,j,[1,2,3]), watch(i,j,[0,2,3]), watch(i,j,[0,1,3]), watch(i,j,[0,1,2])])
        elif data[i][j] == 5:
            all_case.append([watch(i,j,[0,1,2,3])])
dfs(0, set())

print(safe_zone - max_watch)

