def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = ''
        for j in range(n):
            if arr1[i] % 2 == 1 or arr2[i] % 2 == 1:
                a += '#'
            else:
                a += ' '
            arr1[i] //= 2
            arr2[i] //= 2
        answer.append(a[::-1])
    return answer