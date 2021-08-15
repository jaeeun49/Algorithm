# 모든 명령어를 수행한 후 구조물의 상태를 출력
# [x,y,a,b] = a:0은 기둥, 1은 보 / b:0은 삭제, 1은 설치
# 작업을 수행한 결과가 조건을 만족하지 않으면 그 작업은 무시된다.

def impossible(answer):
    for x, y, a in answer:
        if a == 0:  # 기둥
            if y != 0 and (x, y - 1, 0) not in answer and \
                    (x - 1, y, 1) not in answer and (x, y, 1) not in answer:
                return True
        else:  # 보
            if (x, y - 1, 0) not in answer and (x + 1, y - 1, 0) not in answer and \
                    not ((x - 1, y, 1) in answer and (x + 1, y, 1) in answer):
                return True
    return False


def solution(n, build_frame):
    result = set()

    for x, y, a, b in build_frame:
        cnt = (x, y, a)  # return 하는 배열은 [x,y,a] 형식
        if b:  # 추가
            result.add(cnt)
            if impossible(result):
                result.remove(cnt)

        elif cnt in result:  # 삭제
            result.remove(cnt)
            if impossible(result):
                result.add(cnt)
    answer = map(list, result)

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))