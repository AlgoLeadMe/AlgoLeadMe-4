import sys
input = sys.stdin.readline
r,c,w = map(int, input().split())

n = r + w - 1 # 열의 위치 + 변의 개수 (추가될 세로길이) -1 (인덱스 0부터 시작)
dp = [[0] * n for _ in range(n)]

# 초기 세팅 : 양끝 1로 채워주기
dp[0][0] = 1
for i in range(1, n):
    dp[i][0] = 1
    dp[i][i] = 1

# 바로 왼쪽 위와 오른쪽 위의 숫자 합 구하기
for i in range(2, n): 
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

# R,C를 꼭짓점, 변의 길이가 W인 정삼각형 숫자합 구하기
result = 0
for i in range(w):
    for j in range(i+1):
        result += dp[i+r-1][c+j-1]

print(result)