# 한 행 또는 한 열이 지나갈 수 있는 길이 몇개인지를 출력

n,l = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]

answer = 0

for i in range(n):
    first = data[i][0]
    cnt = 1
    for j in range(1,n):
        if data[i][j] == first:
            cnt += 1
        elif data[i][j] == first + 1 and 0 <= cnt:
            if l <= cnt:
                first = data[i][j]
                cnt = 1
            else:
                break
        elif data[i][j] == first - 1 and 0 <= cnt:
            first = data[i][j]
            cnt = -l+1
        else:
            break
    # break를 통해 for문을 빠져나온게 아니면 다음 조건이 성립된다.
    else:
        if 0 <= cnt:
            answer += 1

for j in range(n):
    first = data[0][j]
    cnt = 1
    for i in range(1,n):
        if data[i][j] == first:
            cnt += 1
        elif data[i][j] == first + 1 and 0 <= cnt:
            if l <= cnt:
                first = data[i][j]
                cnt = 1
            else:
                break
        elif data[i][j] == first - 1 and 0 <= cnt:
            cnt = -l+1
            first = data[i][j]
        else:
            break
    else:
        if 0 <= cnt:
            answer += 1
print(answer)