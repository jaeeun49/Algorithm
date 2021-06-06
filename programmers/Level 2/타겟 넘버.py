def dfs(count, cnt, numbers, target):
    global answer
    if count == len(numbers):
        if cnt == target:
            answer += 1
        return

    dfs(count + 1, cnt + numbers[count], numbers, target)
    dfs(count + 1, cnt - numbers[count], numbers, target)


answer = 0
def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return answer