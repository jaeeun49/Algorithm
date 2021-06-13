n = int(input())
data = list(map(int,input().split()))

left = 0
right = n-1
value = abs(data[left] + data[right])
answer_left = left
answer_right = right

while left < right:
    temp = data[left] + data[right]
    if abs(temp) < value:
        answer_left = left
        answer_right = right
        value = abs(temp)
        if value == 0:
            break
    elif temp < 0:
        left += 1
    elif temp > 0:
        right -= 1

print(data[answer_left], data[answer_right])