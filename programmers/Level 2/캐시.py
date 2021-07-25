# 캐시크기에 따른 실행시간을 출력
from collections import deque

def solution(cacheSize, cities):
    q = deque(maxlen = cacheSize)
    answer = 0
    for city in cities:
        city = city.lower()
        if city in q:
            answer += 1
            q.remove(city)
            q.append(city)
        else:
            q.append(city)
            answer += 5
    return answer