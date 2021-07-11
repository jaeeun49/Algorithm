# 초당 최대 처리량을 출력
def check(time, lists):
    c = 0
    start = time
    end = time + 1000
    for a in lists:
        if start <= a[1] and a[0] < end:
            c += 1
    return c

def solution(lines):
    time_list = []
    answer = 1
    for line in lines:
        y, a, b = line.split()
        a = a.split(':')
        b = b.replace('s', '')
        end = (int(a[0]) * 3600 + int(a[1]) * 60 + float(a[2])) * 1000
        start = end - float(b) * 1000 + 1
        time_list.append([start, end])

    for time in time_list:
        answer = max(answer, check(time[0], time_list), check(time[1], time_list))
    return answer