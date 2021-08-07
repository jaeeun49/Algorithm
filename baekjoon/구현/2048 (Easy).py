# 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 출력

from collections import deque
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

q = deque()
def get(x,y):
    if data[x][y]:
        q.append(data[x][y])
        data[x][y] = 0

def merge(x,y,nx,ny):
    while q:
        value = q.popleft()
        if data[x][y] == 0:
            data[x][y] = value
        elif data[x][y] == value:
            data[x][y] += value
            x,y = x+nx, y+ny
        else:
            x,y = x+nx, y+ny
            data[x][y] = value

def move(k):
    if k == 0: # 위로 이동
        for j in range(n):
            for i in range(n):
                get(i,j)
            merge(0,j,1,0)
    elif k == 1: # 아래로 이동
        for j in range(n):
            for i in range(n-1,-1,-1):
                get(i,j)
            merge(n-1,j,-1,0)
    elif k == 2: # 오른쪽으로 이동
        for i in range(n):
            for j in range(n-1,-1,-1):
                get(i,j)
            merge(i,n-1,0,-1)
    elif k == 3: # 왼쪽으로 이동
        for i in range(n):
            for j in range(n):
                get(i,j)
            merge(i,0,0,1)

answer = 0
def solution(count):
    global answer, data
    if count == 5:
        answer = max([max(data[i]) for i in range(n)])
        return

    save = [x[:] for x in data]
    for i in range(4):
        move(i)
        solution(count+1)
        data = [x[:] for x in save]

solution(0)
print(answer)