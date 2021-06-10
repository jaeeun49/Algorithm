def solution(n):
    three = []
    while n:
        three.append(n % 3)
        n //= 3
    three.reverse()
    return sum([three[i] * 3**i for i in range(len(three))])