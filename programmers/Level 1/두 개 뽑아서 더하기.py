# 처음에는 바로 아래와 같이 했는데 테스트케이스 4,5번에서 답이 틀리다고 해서 set의 정렬관련해서 찾아보니
# set은 기존 리스트의 순서를 고려하지 않고 중복만을 제거하기 때문에
# 정렬을 하고 set을 하면 순서가 바뀌게 된다.
# 그러니 set으로 중복을 먼저 없애고 다시 정렬을 해야함!

def solution(numbers):
    answer = [numbers[i] + numbers[j] for i in range(len(numbers)-1) for j in range(i+1,len(numbers))]
    return list(set(sorted(answer)))

# 수정 후
ef solution(numbers):
    answer = [numbers[i] + numbers[j] for i in range(len(numbers)-1) for j in range(i+1,len(numbers))]
    return sorted(list(set(answer)))