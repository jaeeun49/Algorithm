def solution(numbers, hand):
    answer = []
    left,right = [1,4,7], [3,6,9]
    change_2d = {'*':(1,1),0:(1,2),'#':(1,3),
                7:(2,1),8:(2,2),9:(2,3),
                4:(3,1),5:(3,2),6:(3,3),
                1:(4,1),2:(4,2),3:(4,3)}
    h_left, h_right = '*','#'
    for num in numbers:
        if num in right:
            answer.append('R')
            h_right = num
        elif num in left:
            answer.append('L')
            h_left = num
        else:
            r = abs(change_2d[h_right][0]-change_2d[num][0]) + abs(change_2d[h_right][1]-change_2d[num][1])
            l = abs(change_2d[h_left][0]-change_2d[num][0]) + abs(change_2d[h_left][1]-change_2d[num][1])
            if r > l:
                answer.append('L')
                h_left = num
            elif r == l:
                if hand == 'right':
                    answer.append('R')
                    h_right = num
                else:
                    answer.append('L')
                    h_left = num
            else:
                answer.append('R')
                h_right = num
    return ''.join(answer)