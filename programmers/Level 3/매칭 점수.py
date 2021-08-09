import re


def solution(word, pages):
    score = []  # 인덱스(0), URL(1), 기본 점수(2), 링크(3), 링크 수(4)
    for j, k in enumerate(pages):
        k = k.replace('>', '>\n')
        # 1. 해당 url이 무엇인지 먼저 파악 - meta정보에 포함되어있음.
        meta = re.findall('<meta.*', k[k.index('<head>'):k.index('</head>')])
        for i in meta:
            if re.findall('"https://.*"', i):
                url = re.findall('"https://.*"', i)[0][1:-1]  # 앞뒤로 "" 제외해주기 위해서

        # 2. 외부 링크 수 구하기
        link = [i[9:-1] for i in re.findall('<a href="https://.*"', k)]

        # 3. 기본점수 구하기 위해 문자만을 추출
        cnt = re.sub('[^a-zA-Z]', ' ', k).lower().split().count(word.lower())
        score.append([j, url, cnt, link, len(link)])

    res = []
    for x in score:
        # 4. 링크점수 구하기
        link_score = sum(y[2] / y[4] for y in score if y[0] != x[0] and x[1] in y[3])
        res.append([x[0], x[2] + link_score])  # 매칭점수 = 기본점수 + 링크점수
    res.sort(key=lambda x: x[1], reverse=True)

    return res[0][0]