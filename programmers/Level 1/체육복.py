# 최대한 많은 학생이 수업을 들을 수 있도록

# 처음에는 아래와 같이 했는데 테스트케이스 마지막 문제에서 오답이었다.
# 그 이유는 lost에서 하나씩 꺼내서 reserve에 같은지 보기 전에 무조건 제일 처음에 중복을 제거해주어야 한다.
# 만약에 lost = [2,3] reserve = [3] 일때 아래와 같은 코드에서는 2가 먼저 꺼내지므로 3의 체육복을 2가 빌려받게된다.
# 하지만 3은 다른 누구한테도 빌려줄 수 없기 때문에 처음부터 중복을 제거해야함.

def solution(n, lost, reserve):
    lost2 = lost.copy()
    for i in lost:
        if i in reserve:
            lost2.remove(i)
            reserve.remove(i)
        elif i - 1 in reserve:
            lost2.remove(i)
            reserve.remove(i-1)
        elif i + 1 in reserve:
            lost2.remove(i)
            reserve.remove(i+1)
    return n - len(lost2)


# 수정 후
def solution(n, lost, reserve):
    lost2 = [i for i in lost if i not in reserve]
    reserve2 = [i for i in reserve if i not in lost]
    a = []
    for i in lost2:
        if i - 1 in reserve2:
            a.append(i)
            reserve2.remove(i-1)
        elif i + 1 in reserve2:
            a.append(i)
            reserve2.remove(i+1)
    return n - (len(lost2)-len(a))