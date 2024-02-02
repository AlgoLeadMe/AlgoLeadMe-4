n = int(input())
switch = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    gender, num = map(int, input().split())
    if gender == 1:  # 남학생
        for i in range(num-1, len(switch), num):
            switch[i] = 1 - switch[i]
    elif gender == 2:  # 여학생
        num -= 1
        left = right = num
        while switch[left] == switch[right]:
            switch[left] = 1 - switch[left]
            switch[right] = 1 - switch[right]
            left -= 1
            right += 1
        switch[num] = 1 - switch[num]


for i in range(0, n, 20):
    print(' '.join(map(str, switch[i:i+20])))
