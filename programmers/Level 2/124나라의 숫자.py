def solution(n):
    a = ['1', '2', '4']
    index = []
    while n != 0:
        index.append((n - 1) % 3)
        n = (n - 1) // 3
    index.reverse()

    answer = ''
    for i in index:
        answer += a[i]
    answer = ''.join(answer)
    return answer