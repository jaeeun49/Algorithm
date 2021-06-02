n = int(input())
data = [list(input().split()) for _ in range(n)]
# 국 영 수 점수를 숫자로 바꾸기
data = list(map(lambda x: (x[0], int(x[1]), int(x[2]), int(x[3])), data))

data = sorted(data, key = lambda x: (-x[1], x[2], -x[3], x[0]))
for i in data:
    print(i[0])


