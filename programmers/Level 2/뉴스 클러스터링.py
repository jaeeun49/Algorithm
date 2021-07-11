# 다중집합에 대해서 교집합의 크기를 합집합의 크기로 나눈 값을 출력
# 입력으로 들어온 문자열을 두 글자씩 끊어서 다중집합 원소로 만든다.
import math

def solution(str1, str2):
    str1 = [str1[i:i + 2].lower() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    str2 = [str2[i:i + 2].lower() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]

    union = set(str1) | set(str2)
    inter = set(str1) & set(str2)

    # 모두 공집합이면 자카드 유사도는 1이므로 미리 처리
    if len(union) == 0:
        return 65536

    # 중복된 단어를 count해서 실제 다중집합 합집합과 교집합 원소의 개수를 구한다.
    union = sum([max(str1.count(a), str2.count(a)) for a in union])
    inter = sum([min(str1.count(a), str2.count(a)) for a in inter])

    return math.floor((inter / union) * 65536)