# 스테이지에 도달한 유저가 없으면 밑에 users가 0이기때문에 나눌 수 없다
# 그래서 user가 0일때, 아닐때로 나누어야 한다

def solution(N, stages):
    answer = []
    users = len(stages)
    for i in range(1,N+1):
        if users == 0:
            answer.append((i,0))
        else:
            answer.append((i, stages.count(i) / users))
        users -= stages.count(i)
    answer = sorted(answer, key = lambda x: x[1], reverse = True)
    return list(map(lambda x: x[0], answer))