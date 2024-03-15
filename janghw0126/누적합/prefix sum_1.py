import sys
input = sys.stdin.readline
# 각각의 수들을 입력받는다.
n,k,q,m = map(int, input().split())
# 졸고있는 학생들과 출석 코드를 받을 학생들을 초기화한다.
sleep = [0]*(n+3)
check = [0]*(n+3)

for i in map(int, input().split()):
    sleep[i] = 1
for i in map(int, input().split()):
    if sleep[i]: 
        continue
    for j in range(i, n+3, i):
        if not sleep[j]:
            check[j] = 1

prefix = [check[0]]
for i in range(1, n+3):
    # 각 번호 i까지 출석한 학생들의 합을 구한다.
    prefix.append(prefix[-1]+check[i])

for _ in range(m):
    # s부터 e까지 결석한 학생들의 합을 구한다.
    s, e = map(int, input().split()) 
    # 전체 - (s부터 e까지 출석한 학생들)을 출력해준다.
    print(e-s+1 - (prefix[e]-prefix[s-1])) 