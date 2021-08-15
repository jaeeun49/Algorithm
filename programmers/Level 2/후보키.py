def solution(relation):
    answer = []

    # 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1100, 1110,..., 1111까지
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):  # 유일성을 만족하는지
            not_duplicate = True
            for num in answer:
                if (num & i) == num:  # 최소성을 만족하는지
                    not_duplicate = False
                    break
            if not_duplicate:
                answer.append(i)
    return len(answer)