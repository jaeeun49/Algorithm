# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return

def solution(board, moves):
    moves = list(map(lambda x: x - 1, moves))
    basket = [0]
    answer = 0

    for col in moves:
        row = 0
        while row < len(board):
            if board[row][col] != 0:
                if basket[-1] == board[row][col]:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(board[row][col])
                board[row][col] = 0
                break
            row += 1
    return answer