# 9:00시부터 총 n회 t분 간격으로 역에 도착
# 콘이 셔틀을 타고 사무실로 갈 수 있는 도착시간 중 제일 늦은 시각을 출력

def solution(n, t, m, timetable):
    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    timetable.sort()
    last_time = 9 * 60 + (n - 1) * t  # 마지막 셔틀시간

    for i in range(n):  # 셔틀버스 횟수만큼 반복
        # 1. 기다리고 있는 크루 다 태울 수 있으면 콘은 마지막 셔틀시간에 맞춰오면 됨
        if len(timetable) < m:
            return '%02d:%02d' % (last_time // 60, last_time % 60)

        # 2. 마지막 버스인데 아직 타야하는 크루가 있으면 m번째 크루보다 1분 빨리오면 됨
        elif i == n - 1:
            if timetable[m - 1] <= last_time:
                last_time = timetable[m - 1] - 1
            return '%02d:%02d' % (last_time // 60, last_time % 60)

        # 태울 수 있는 크루먼저 태워 보내기 보내기
        for j in range(m - 1, -1, -1):
            if timetable[j] <= 9 * 60 + i * t:
                del timetable[j]