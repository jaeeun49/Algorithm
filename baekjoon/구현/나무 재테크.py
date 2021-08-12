# m개의 나무를 심었다. 같은 칸에 여러 개의 나무가 심어질 수 있다.
# k년이 지난 후, 땅에 살아있는 나무의 개수를 출력

n,m,k = map(int,input().split())

# 3가지를 고려해야 한다.
# 1.땅에 있는 양분의 양을 담는 변수
# 2. 매년 겨울마다 추가되는 양분의 양을 담는 변수 - 입력으로 주어짐
# 3. 나무의 위치와 나이 정보를 담는 변수 - 입력으로 주어짐
nutri = [[5 for _ in range(n)] for _ in range(n)]
A = [list(map(int,input().split())) for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,age = map(int,input().split())
    tree[x-1][y-1].append(age)

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(k):
    # 봄: 자신의 나이만큼 양분을 먹고 나이가 1 증가. 나이가 어린 나무부터 양분을 먹는다
    # 여름: 땅에 양분이 부족해 나이만큼 양분을 먹지 못해 죽은 나무의 나이를 2로 나눈 값만큼 같은 같네 양분으로 추가
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree[i][j].sort()
                new_tree, dead_tree = [],0
                for age in tree[i][j]:
                    if age <= nutri[i][j]:
                        nutri[i][j] -= age
                        new_tree.append(age+1)
                    else:
                        dead_tree += age//2
                tree[i][j] = []
                tree[i][j].extend(new_tree)
                nutri[i][j] += dead_tree

    # 가을: 나이가 5의 배수인 나무들의 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for age in tree[i][j]:
                    if age % 5 == 0:
                        for d in range(8):
                            nx,ny = i+dx[d], j+dy[d]
                            if 0 <= nx < n and 0 <= ny < n:
                                tree[nx][ny].append(1)

    # 겨울: A만큼 땅에 양분이 추가된다.
    for i in range(n):
        for j in range(n):
            nutri[i][j] += A[i][j]

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(tree[i][j])
print(answer)