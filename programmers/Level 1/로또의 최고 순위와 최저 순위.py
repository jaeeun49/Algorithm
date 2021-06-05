def solution(lottos, win_nums):
    count = 0
    zero = lottos.count(0)
    lottos = [x for x in lottos if x != 0]
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    for num in lottos:
        if num in win_nums:
            count += 1
    return rank[count + zero],rank[count]