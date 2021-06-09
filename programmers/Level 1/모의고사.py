def solution(answers):
    m1 = [1, 2, 3, 4, 5]
    m2 = [2, 1, 2, 3, 2, 4, 2, 5]
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count = []
    count.append(sum([answers[i] == m1[i % 5] for i in range(len(answers))]))
    count.append(sum([answers[i] == m2[i % 8] for i in range(len(answers))]))
    count.append(sum([answers[i] == m3[i % 10] for i in range(len(answers))]))

    max_value = max(count)
    answer = []
    for index, value in enumerate(count):
        if value == max_value:
            answer.append(index + 1)
    return answer