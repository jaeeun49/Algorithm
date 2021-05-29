to_day = [0,0,31,60,91,121,152,182,213,244,274,305,335]
weekday = ['THU','FRI','SAT','SUN','MON','TUE','WED']

def solution(a, b):
    day = to_day[a] + b
    return weekday[day % 7]