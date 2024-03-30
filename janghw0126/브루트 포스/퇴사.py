n = int(input())
t = []
p = []
for i in range(n) :
    arr = list(map(int, input().split()))
    t.append(arr[0])
    p.append(arr[1])
ans = 0

# 재귀함수 사용
def go(day, sum) :
    global ans
    if day == n :
        ans = max(ans,sum)
        return
    if day > n :
        return
    go(day+t[day], sum+p[day])
    go(day+1, sum)
    
go(0,0)
print(ans)