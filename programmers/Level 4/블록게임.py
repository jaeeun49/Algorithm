# 검은 블록을 떨어뜨려 없앨 수 있는 블록의 개수의 최댓값을 출력
import numpy as np


def solution(board):
    answer = 0
    blocks = {}
    # 다음과 같이 각 번호에 해당하는 4개의 블록 위치 정보가 들어간다.
    # 1: {'left': 0, 'right': 2, 'top': 8, 'bottom': 9, 'coords': [[8, 0], [9, 0], [9, 1], [9, 2]]}

    for i, row in enumerate(board):
        for j, number in enumerate(row):
            if number > 0:
                if number not in blocks:
                    blocks[number] = {'left': 51, 'right': -1, 'top': 51, 'bottom': -1, 'coords': []}
                blocks[number]['left'] = min(blocks[number]['left'], j)
                blocks[number]['right'] = max(blocks[number]['right'], j)
                blocks[number]['top'] = min(blocks[number]['top'], i)
                blocks[number]['bottom'] = max(blocks[number]['bottom'], i)
                blocks[number]['coords'].append([i, j])
    for i in range(len(board)):
        print(board[i])
    print(blocks)

    board = np.array(board)
    removed = 1
    while removed > 0:
        removed = 0
        # 각각의 블록 넘버에 대해서 4개의 좌표를 이용해서 직사각형 구역안을 탐색
        for block_key in blocks:
            can_remove = True
            block = blocks[block_key]
            zeros = 0
            for i in range(block['top'], block['bottom'] + 1):
                for j in range(block['left'], block['right'] + 1):
                    if board[i][j] == 0:
                        zeros += 1
                        if (board[:i, j] > 0).any():
                            can_remove = False
                            break
                if not can_remove:
                    break

            # 만약 관할 직사각형 구간에 빈칸이 2개이고 제거할 수 있는 상태이면
            if can_remove and zeros == 2:
                for coord in blocks[block_key]['coords']:
                    board[coord[0]][coord[1]] = 0
                del blocks[block_key]

                removed += 1
                answer += 1
                break
    return answer