# 전체 상담 가능한 날짜 수를 입력받는다.
n = int(input()) 
# 각 상담을 완료하는데 걸리는 기간을 초기화한다.
t = []
# 각 상담을 했을 때 받을 수 있는 금액을 초기화한다.
p = []
for i in range(n) :
    # 상담 기간과 금액을 입력받는다.
    arr = list(map(int, input().split()))
    # 상담 기간을 저장한다.
    t.append(arr[0])
    # 상담 금액을 저장한다.
    p.append(arr[1])
# 최대 이익 저장 변수를 선언한다.
ans = 0 

# 재귀 함수를 정의한다.
def go(day, sum) :
    # 전역 변수로 ans를 사용한다.
    global ans
    # 모든 날짜를 확인했을 때 현재까지의 이익과 최대 이익을 비교하여 갱신한다.
    if day == n :
        ans = max(ans,sum) 
        return
    # 상담 기간이 남은 기간을 초과할 경우, 더 이상 진행 불가하므로 함수를 종료한다.
    if day > n :
        return
    # 해당 날짜의 상담을 진행하는 경우
    go(day+t[day], sum+p[day]) 
    # 해당 날짜의 상담을 진행하지 않는 경우
    go(day+1, sum) 
    
# 재귀 함수를 호출한다.
go(0,0) 
# 최대 이익을 출력한다.
print(ans)