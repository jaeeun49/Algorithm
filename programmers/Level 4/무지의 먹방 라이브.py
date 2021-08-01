def solution(food_times, k):
    if sum(food_times) <= k: return -1

    time = sorted([(idx, val) for idx, val in enumerate(food_times)], key=lambda x: x[1])
    idx = 0
    n = len(food_times)
    cycle = time[0][1]
    while k - (n * cycle) > 0:
        k -= n * cycle
        n -= 1
        idx += 1
        cycle = time[idx][1] - time[idx - 1][1]
    return [i[0] + 1 for i in sorted(time[idx:])][k % n]