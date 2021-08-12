# 몇 번째 단계가 진행 중일 때, 종료되는지를 출력

from collections import deque
n,k = map(int,input().split())
A = deque(map(int,input().split()))
robot = deque([0 for _ in range(2 * n)])

turn = 1
while 1:
    # 1. 벨트가 로봇과 함께 회전한다.
    robot.rotate(1)
    A.rotate(1)
    robot[n-1] = 0

    # 2. 먼저 올라간 로봇부터 회전하는 방향으로 한칸 이동
    for i in range(n-2,-1,-1):
        if robot[i] == 1 and robot[i+1] == 0 and 0 < A[i+1]:
            robot[i] = 0
            robot[i+1] = 1
            A[i+1] -= 1
    robot[n-1] = 0

    # 3. 올리는 위치의 내구도가 0이 아니면 로봇 올리기
    if 0 < A[0]:
        robot[0] = 1
        A[0] -= 1

    # 4. 내구도가 0인 칸의 개수가 k개 이상이면 과정을 종료
    if k <= A.count(0):
        print(turn)
        break

    turn += 1