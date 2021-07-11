def change(a):
    a = a.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return a

def solution(m, musicinfos):
    m = change(m)
    answer = ('(None)',None)
    for info in musicinfos:
        start,end,title,melody = info.split(',')
        start_h,start_m,end_h,end_m = map(int,start.split(':')+end.split(':'))
        time = 60*(end_h-start_h) + (end_m-start_m)
        melody = change(melody)
        melody_played = (melody*time)[:time]
        if m in melody_played:
            if (answer[1]==None) or (time>answer[1]):
                answer = (title, time)
    return answer[0]