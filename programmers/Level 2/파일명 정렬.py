import re

def solution(files):
    files = [re.split(r'([0-9]+)', f) for f in files]
    files = sorted(files, key = lambda x: (x[0].lower(), int(x[1])))
    return [''.join(f) for f in files]