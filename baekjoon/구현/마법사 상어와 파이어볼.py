def solution(n,m,k,balls):
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    # k번 이동을 명령한다.
    for _ in range(k):
        positions = {} # 이동이 끝난 파이어볼의 위치가 담긴다.
        # 모든 파이어볼이 자신의 방향으로 속력만큼 이동한다
        for x,y,m,s,d in balls:
            nx,ny = (x+dx[d]*s) % n, (y+dy[d]*s) % n # 1번(행,열)은 n번(행,열)과 연결되어있다.
            positions.setdefault((nx,ny),[]).append([m,s,d])

        new_balls = []
        for (x,y),vals in positions.items():
            # 그 자리에 파이어볼이 하나만 있으면 그대로 new_balls에 담는다
            if len(vals) == 1:
                new_balls.append((x,y,*vals[0]))
                continue

            nm,ns,nd = 0,0,[]
            for m,s,d in vals:
                nm += m
                ns += s
                nd.append(d % 2)
            nm //= 5
            ns //= len(vals)
            nd = [0,2,4,6] if all(x == nd[0] for x in nd) else [1,3,5,7]
            if nm > 0:
                for d in nd:
                    new_balls.append((x,y,nm,ns,d))
        balls = new_balls
    return sum([x[2] for x in balls])


n,m,k = map(int,input().split())
balls = [list(map(int,input().split())) for _ in range(m)]
balls = [(x[0]-1, x[1]-1, *x[2:]) for x in balls]
print(solution(n,m,k,balls))