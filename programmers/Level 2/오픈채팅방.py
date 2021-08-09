def solution(record):
    answer = []
    names = {}
    a = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    for r in record:
        r = r.split(' ')
        if r[0] in ['Enter', 'Change']:
            names[r[1]] = r[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(names[r.split(' ')[1]] + a[r.split(' ')[0]])

    return answer