# 상어가 먹을 수 있는 물고기 번호 합의 최댓값을 출력
from copy import deepcopy

data = [[] for _ in range(4)]
for i in range(4):
    a = list(map(int,input().split()))
    for j in range(4):
        data[i].append([a[j*2], a[j*2+1]-1])

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def find_fish(number, data):
    for i in range(4):
        for j in range(4):
            if data[i][j][0] == number:
                return i,j
    return

def turn(direction):
    return (direction + 1) % 8

def move(now_x, now_y, data):
    # 물고기가 번호가 작은 순서대로 이동한다
    for i in range(1, 17):
        position = find_fish(i, data)
        if position is not None: # 상어가 먹었으면 그 숫자의 물고기가 없을 수도 있으니까
            x,y = position
            d = data[x][y][1]
            for _ in range(8):
                nx,ny = x+dx[d], y+dy[d]
                data[x][y][1] = d
                if 0 <= nx < 4 and 0 <= ny < 4: # 경계를 넘지 않으면서
                    if not (nx == now_x and ny == now_y): # 이동하려는 자리에 상어가 없으면
                        data[x][y], data[nx][ny] = data[nx][ny], data[x][y] # 자리 이동
                        break
                d = turn(d)

def get_possible_positions(now_x, now_y, data):
    positions = []
    d = data[now_x][now_y][1]
    for _ in range(3):
        now_x += dx[d]
        now_y += dy[d]
        if 0 <= now_x < 4 and 0 <= now_y < 4 and data[now_x][now_y][0] != -1: # 물고기가 있어야 함!
            positions.append((now_x, now_y))
    return positions

answer = 0
def solve(now_x, now_y, cnt, data):
    global answer
    data = deepcopy(data)

    # 1. 상어는 현재 위치에 물고기를 먹는다
    cnt += data[now_x][now_y][0]
    data[now_x][now_y][0] = -1

    # 2. 모든 물고기가 이동한다
    move(now_x, now_y, data)

    # 3. 물고기 이동이 모두 끝나면 상어가 이동한다
    positions = get_possible_positions(now_x, now_y, data)

    # 상어가 이동할 수 있는 칸이 없으면 끝
    if len(positions) == 0:
        answer = max(answer, cnt)
        return

    for next_x,next_y in positions:
        solve(next_x, next_y, cnt, data)

solve(0,0,0,data)
print(answer)