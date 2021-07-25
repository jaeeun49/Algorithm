def solution(words):
    words.sort()
    answer = 0
    for idx,word in enumerate(words):
        cnt = 1
        if 0 < idx:
            cnt = max(cnt, check(word, words[idx-1]))
        if idx < len(words)-1:
            cnt = max(cnt, check(word, words[idx+1]))
        answer += cnt
    return answer

def check(a,b):
    for i,char in enumerate(a):
        if len(b)==i or char != b[i]:
            return i+1
    return len(a)