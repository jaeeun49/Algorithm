from collections import Counter

def solution(participant, completion):
    A = Counter(participant)
    B = Counter(completion)
    answer = A-B
    return [x for x in answer.keys()][0]