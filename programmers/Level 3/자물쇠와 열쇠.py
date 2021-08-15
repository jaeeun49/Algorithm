def attach(k, x, y, key, board):
    for i in range(k):
        for j in range(k):
            board[x + i][y + j] += key[i][j]


def detach(k, x, y, key, board):
    for i in range(k):
        for j in range(k):
            board[x + i][y + j] -= key[i][j]


def rotate(arr):
    return list(zip(*arr[::-1]))


def possible(board, l, k):
    for i in range(l):
        for j in range(l):
            if board[k + i][k + j] != 1:
                return False
    return True


def solution(key, lock):
    k, l = len(key), len(lock)
    board = [[0] * (k * 2 + l) for _ in range(k * 2 + l)]

    # board 중앙 부분에 lock 배치시키기
    for i in range(l):
        for j in range(l):
            board[k + i][k + j] = lock[i][j]

    rotated = key
    for _ in range(4):  # 4방향에 대해서
        rotated = rotate(rotated)
        # 키 넣기
        for x in range(1, k + l):
            for y in range(1, k + l):
                attach(k, x, y, rotated, board)
                if possible(board, l, k):
                    return True
                detach(k, x, y, rotated, board)
    return False